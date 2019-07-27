# -*- coding: utf-8 -*-

import json
from countries import country_codes

with open('cities.json', 'r', encoding='utf-8') as cities_json:
	with open('selected_city_codes.py', 'w', encoding='utf-8') as selected_city_codes_file:
		cities = json.loads(cities_json.read())
		selected_city_codes_file.write('[')
		needed_cities = []
		for country in country_codes:
			for city in cities:
				if country == city['country_code']:
					needed_cities.append(city)
					selected_city_codes_file.write("'{}', ".format(city['code']))
		selected_city_codes_file.write(']')




