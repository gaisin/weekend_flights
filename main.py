# -*- coding: utf-8 -*-

import requests
import json
import datetime
import time
import logging
from private import *

# списки выходных дней
from weekends import weekends, may_weekends, weekday_names

# списки направлений, по которым я хочу или не хочу искать билеты, а также словари для преобразования IATA кодов в русские названия
from destinations import willing_countries, willing_cities, unwilling_destinations, cities_code_to_name_dict, countries_code_to_name_dict


root_logger= logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = logging.FileHandler('C:\wknd\main.log', encoding='utf-8')
formatter = logging.Formatter('LINE:%(lineno)3d # %(levelname)-8s [%(asctime)s]  %(message)s')
handler.setFormatter(formatter)
root_logger.addHandler(handler)


def post_to_vk(flights_data, notice='Билет'):
    root_logger.debug('Func "post_to_vk" has started')
    root_logger.debug('got flights_data as input: {}'.format(flights_data))

    for flight in flights_data:
        data = '{notice}: {origin} - {destination}, '\
                'c {depart_date} ({depart_week_day}) '\
                'по {return_date} ({return_week_day}) за {value} рублей: '\
                '{link}'.format(
                        notice=notice,
                        origin=flight['origin'],
                        destination=flight['destination'],
                        depart_date=flight['depart_date'],
                        depart_week_day=flight['depart_week_day'],
                        return_date=flight['return_date'],
                        return_week_day=flight['return_week_day'], 
                        value=flight['value'],
                        link=flight['link']
                    )

        response = requests.post('https://api.vk.com/method/wall.post', data={'access_token': VK_TOKEN,
                                                                            'owner_id': VK_OWNER_ID_GROUP,
                                                                            'from_group': 1,
                                                                            'message': data,
                                                                            'signed': 0,
                                                                            'v':"5.52"}).json()
        root_logger.debug(response)
        time.sleep(1)

    root_logger.debug('Func "post_to_vk" has finished')


def post_to_ifttt_notification(flights_data, notice='Билет'):
    for flight in flights_data:
        ifttt_event_url = 'https://maker.ifttt.com/trigger/ticket_found/with/key/{}'.format(IFTTT_KEY)
        flight_info = '{notice}: Москва - {destination} за {price}р., {depart_date} ({depart_week_day})'\
                      '-{return_date} ({return_week_day})'.format(
                                notice=notice,
                                destination=flight['destination'],
                                price=flight['value'],
                                depart_date=flight['depart_date'],
                                depart_week_day=flight['depart_week_day'],
                                return_date=flight['return_date'],
                                return_week_day=flight['return_week_day']
                        )
        data_to_send = {
            'value1': flight_info
        }
        root_logger.debug('Flight info to send to IFTTT: '.format(flight_info))
        # Отправка запроса HTTP POST в URL вебхука
        requests.post(ifttt_event_url, json=data_to_send)


def print_flights(flights_data, notice='Билет'):
    if len(flights_data) == 0:
        print('{}: ничего не найдено'.format(notice))
    else:
        for flight in flights_data:
            flight_info = '{notice}: Москва - {destination} за {price}р., {depart_date} ({depart_week_day})'\
                          '-{return_date} ({return_week_day})'.format(
                                    notice=notice,
                                    destination=flight['destination'],
                                    price=flight['value'],
                                    depart_date=flight['depart_date'],
                                    depart_week_day=flight['depart_week_day'],
                                    return_date=flight['return_date'],
                                    return_week_day=flight['return_week_day']
                            )
            print(flight_info)


def get_latest_flights(destination_codes, months):
    root_logger.debug('Func "get_latest_prices_of_month" has started')
    # cheapest flights for last 48 hours, documentation: https://support.travelpayouts.com/hc/ru/articles/203956163#02
    url='http://api.travelpayouts.com/v2/prices/latest'

    found_flights = []

    for key in months.keys():
        root_logger.debug('Starting to check flights in {}'.format(key))
        for code in destination_codes:
            destination = code
            root_logger.debug('Collecting flights to {} in {}'.format(destination, key))

            # Переделать этот костыль с try-except!
            try:
                root_logger.debug('Searching flights to {}'.format(countries_code_to_name_dict[destination]))
            except:
                root_logger.debug('Searching flights to {}'.format(destination))

            payload = {
                'token': TRAVELPAYOUTS_TOKEN, 
                'origin': 'MOW',
                'destination': destination,
                'beginning_of_period': months[key],
                'period_type': 'month',  
                'limit': 1000
            }
            response = requests.get(url, params=payload)
            flights_raw = response.json()
            flights_data = flights_raw['data']
            root_logger.debug('Found {} flights'.format(len(flights_data)))
            found_flights += flights_data

    root_logger.debug('Func "get_latest_prices_of_month" has finished')
    return found_flights


def find_weekend_flights(flights_data, days, max_value):
    root_logger.debug('Func "find_weekend_flights" has started')

    found_flights = []

    for flight in flights_data:
        # this is because sometimes flight becomes a string
        if isinstance(flight, str):
            root_logger.debug('flight is string')
            continue
        root_logger.debug('flight to {} is dict'.format(flight['destination']))
        root_logger.debug('Flight: {}'.format(flight))

        found_at = flight['found_at']

        try:
            found_at_datetime = datetime.datetime.strptime(found_at, '%Y-%m-%dT%H:%M:%S')
        except:
            found_at_datetime = datetime.datetime.strptime(found_at, '%Y-%m-%dT%H:%M:%S.%f')
        
        time_now = datetime.datetime.now()
        time_difference = time_now - found_at_datetime
        time_difference_in_hours = time_difference / datetime.timedelta(hours=1)

        if time_difference_in_hours <= 6 and flight['value'] <= max_value and flight['destination'] not in unwilling_destinations:
            for date in days:
                if flight['depart_date'] == date[0] and flight['return_date'] == date[1]:
                    depart_date_formatted = ''.join(reversed(flight['depart_date'][5:].split('-')))
                    return_date_formatted = ''.join(reversed(flight['return_date'][5:].split('-')))

                    depart_date_str_list = flight['depart_date'].split('-')
                    depart_date_int_list = [int(elem) for elem in depart_date_str_list]
                    depart_date = datetime.date(depart_date_int_list[0], depart_date_int_list[1], depart_date_int_list[2])
                    depart_week_day = depart_date.isoweekday()

                    return_date_str_list = flight['return_date'].split('-')
                    return_date_int_list = [int(elem) for elem in return_date_str_list]
                    return_date = datetime.date(return_date_int_list[0], return_date_int_list[1], return_date_int_list[2])
                    return_week_day = return_date.isoweekday()

                    origin = cities_code_to_name_dict[flight['origin']]
                    destination = cities_code_to_name_dict[flight['destination']]

                    root_logger.debug('{origin} - {destination} '\
                        'from {depart_date} ({depart_week_day}) '\
                        'to {return_date} ({return_week_day}) '\
                        'for {value} rub'.format(
                                origin=origin,
                                destination=destination,
                                depart_date=flight['depart_date'],
                                depart_week_day=weekday_names[depart_week_day],
                                return_date=flight['return_date'],
                                return_week_day=weekday_names[return_week_day],
                                value=flight['value']
                            ))
                    link = 'https://www.aviasales.ru/search/{}{}{}{}1?marker=207849'.format(
                        flight['origin'],
                        depart_date_formatted,
                        flight['destination'],
                        return_date_formatted
                    )
                    root_logger.debug(link)
                    root_logger.debug('Flight found at {}'.format(flight['found_at']))

                    flight_dict = {
                        'origin': origin,
                        'destination': destination,
                        'depart_date': flight['depart_date'],
                        'depart_week_day': weekday_names[depart_week_day],
                        'return_date': flight['return_date'],
                        'return_week_day': weekday_names[return_week_day],
                        'value': flight['value'],
                        'link': link
                    }
                    found_flights.append(flight_dict)
                    
    root_logger.debug('Func "find_weekend_flights" has finished, found {} flights'.format(len(found_flights)))
    return found_flights


def main():
    root_logger.info('Func "main" has started')

    months = {
        'february': '2019-02-01',
        'march': '2019-03-01',
        'april': '2019-04-01',
        'may': '2019-05-01',
        'june': '2019-06-01',
        # лучше сократить месяцы, т.к. все равно пока не планирую ничего позже июня
        # 'july': '2019-07-01',
        # 'august': '2019-08-01',
        # 'september': '2019-09-01',
        # 'october': '2019-10-01',
        # 'november': '2019-11-01',
        # 'december': '2019-12-01'
    }

    willing_destinations = willing_countries + willing_cities

    flights_data = get_latest_flights(willing_destinations, months)

    root_logger.info('Найдено {} билетов по России и Европе'.format(len(flights_data)))

    # для всех выходных
    max_weekend_ticket_price = 4000
    weekend_flights = find_weekend_flights(flights_data, weekends, max_weekend_ticket_price)
    root_logger.debug('Weekend flights:\n{}'.format(weekend_flights))
    weekend_notice = 'На выходные'
    post_to_vk(weekend_flights, weekend_notice)
    post_to_ifttt_notification(weekend_flights, weekend_notice)
    print_flights(weekend_flights, weekend_notice)
    root_logger.info('Найденные билеты на выходные:\n{}'.format(weekend_flights))

    # для майских
    max_may_weekend_ticket_price = 8000
    may_weekend_flights = find_weekend_flights(flights_data, may_weekends, max_may_weekend_ticket_price)
    root_logger.debug('\n\nMay weekend flights:\n{}'.format(may_weekend_flights))
    may_notice = 'На майские'
    post_to_vk(may_weekend_flights, may_notice)
    post_to_ifttt_notification(may_weekend_flights, may_notice)
    print_flights(may_weekend_flights, may_notice)
    root_logger.info('Найденные билеты на майские:\n{}'.format(may_weekend_flights))

    # В Уфу
    ufa_flights_data = get_latest_flights(['UFA'], months)
    root_logger.info('Найдено {} билетов в Уфу'.format(len(ufa_flights_data)))

    # на выходных в Уфу
    max_ufa_ticket_price = 3500
    ufa_weekend_flights = find_weekend_flights(ufa_flights_data, weekends, max_ufa_ticket_price)
    root_logger.debug('\n\nUfa weekend flights:\n{}'.format(ufa_weekend_flights))
    ufa_notice = 'В Уфу на выходные'
    post_to_vk(ufa_weekend_flights, ufa_notice)
    post_to_ifttt_notification(ufa_weekend_flights, ufa_notice)
    print_flights(ufa_weekend_flights, ufa_notice)
    root_logger.info('Найденные билеты на выходные в Уфу:\n{}'.format(ufa_weekend_flights))

    # на майских в Уфу
    max_may_ufa_ticket_price = 6000
    ufa_may_weekend_flights = find_weekend_flights(ufa_flights_data, may_weekends, max_may_ufa_ticket_price)
    root_logger.debug('\n\nUfa weekend flights:\n{}'.format(ufa_may_weekend_flights))
    ufa_may_notice = 'В Уфу на майские'
    post_to_vk(ufa_may_weekend_flights, ufa_may_notice)
    post_to_ifttt_notification(ufa_may_weekend_flights, ufa_may_notice)
    print_flights(ufa_may_weekend_flights, ufa_may_notice)
    root_logger.info('Найденные билеты на майские в Уфу:\n{}'.format(ufa_may_weekend_flights))

    root_logger.info('Func "main" has finished\n\n\n')


def test_run():
    root_logger.info('Func "test_run" has started')

    months = {
        'february': '2019-02-01'
    }

    ufa_flights_data = get_latest_flights(['UFA'], months)
    max_ufa_ticket_price = 5000
    ufa_weekend_flights = find_weekend_flights(ufa_flights_data, weekends, max_ufa_ticket_price)
    root_logger.debug('\n\nUfa weekend flights:\n{}'.format(ufa_weekend_flights))
    ufa_notice = 'В Уфу на выходные'
    post_to_vk(ufa_weekend_flights, ufa_notice)
    post_to_ifttt_notification(ufa_weekend_flights, ufa_notice)
    print_flights(ufa_weekend_flights, ufa_notice)
    root_logger.info('Найденные билеты на выходные в Уфу:\n{}'.format(ufa_weekend_flights))

    root_logger.info('Func "test_run" has finished\n\n\n')


def show_unwilling_destionations():
    for city in unwilling_destinations:
        print(cities_code_to_name_dict[city])


if __name__ == '__main__':
    main()
    # test_run()
    # show_unwilling_destionations()
