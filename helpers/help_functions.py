# -*- coding: utf-8 -*-

def time_str_to_datetime():
    # преобразовать формат из str в datetime
    found_at = '2019-01-30T09:30:10'
    found_at_datetime = datetime.datetime.strptime(found_at, '%Y-%m-%dT%H:%M:%S')
    
    time_now = datetime.datetime.now()
    time_difference = time_now - found_at_datetime
    time_difference_in_hours = time_difference / datetime.timedelta(hours=1)

    print(type(found_at_datetime))
    print(found_at_datetime)
    print(time_now)
    print(type(time_difference_in_hours))
    print(time_difference_in_hours)


def daterange(start_date, end_date):
    # вспомогательная функция для функции weekends
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def weekends():
    # для того, чтобы сделать список дней с пятницы по понедельник
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2019, 12, 31)
    for single_date in daterange(start_date, end_date):
        if single_date.isoweekday() in [1, 5, 6, 7]:
            print(single_date.strftime("%Y-%m-%d"))
        if single_date.isoweekday() in [1, 4]:
            print()
        '''
        if single_date.isoweekday() == (1 or 5 or 6 or 7):
            single_weekend_options.append(single_date.strftime("%Y-%m-%d"))
        else: 
            if single_weekend_options:
                weekends.append(single_weekend_options)
        '''

