# -*- coding: utf-8 -*-

weekends = [('2019-01-04', '2019-01-07'), ('2019-01-04', '2019-01-06'), ('2019-01-05', '2019-01-07'), ('2019-01-05', '2019-01-06'), ('2019-01-11', '2019-01-14'), ('2019-01-11', '2019-01-13'), ('2019-01-12', '2019-01-14'), ('2019-01-12', '2019-01-13'), ('2019-01-18', '2019-01-21'), ('2019-01-18', '2019-01-20'), ('2019-01-19', '2019-01-21'), ('2019-01-19', '2019-01-20'), ('2019-01-25', '2019-01-28'), ('2019-01-25', '2019-01-27'), ('2019-01-26', '2019-01-28'), ('2019-01-26', '2019-01-27'), ('2019-02-01', '2019-02-04'), ('2019-02-01', '2019-02-03'), ('2019-02-02', '2019-02-04'), ('2019-02-02', '2019-02-03'), ('2019-02-08', '2019-02-11'), ('2019-02-08', '2019-02-10'), ('2019-02-09', '2019-02-11'), ('2019-02-09', '2019-02-10'), ('2019-02-15', '2019-02-18'), ('2019-02-15', '2019-02-17'), ('2019-02-16', '2019-02-18'), ('2019-02-16', '2019-02-17'), ('2019-02-22', '2019-02-25'), ('2019-02-22', '2019-02-24'), ('2019-02-23', '2019-02-25'), ('2019-02-23', '2019-02-24'), ('2019-03-01', '2019-03-04'), ('2019-03-01', '2019-03-03'), ('2019-03-02', '2019-03-04'), ('2019-03-02', '2019-03-03'), ('2019-03-08', '2019-03-11'), ('2019-03-08', '2019-03-10'), ('2019-03-09', '2019-03-11'), ('2019-03-09', '2019-03-10'), ('2019-03-15', '2019-03-18'), ('2019-03-15', '2019-03-17'), ('2019-03-16', '2019-03-18'), ('2019-03-16', '2019-03-17'), ('2019-03-22', '2019-03-25'), ('2019-03-22', '2019-03-24'), ('2019-03-23', '2019-03-25'), ('2019-03-23', '2019-03-24'), ('2019-03-29', '2019-04-01'), ('2019-03-29', '2019-03-31'), ('2019-03-30', '2019-04-01'), ('2019-03-30', '2019-03-31'), ('2019-04-05', '2019-04-08'), ('2019-04-05', '2019-04-07'), ('2019-04-06', '2019-04-08'), ('2019-04-06', '2019-04-07'), ('2019-04-12', '2019-04-15'), ('2019-04-12', '2019-04-14'), ('2019-04-13', '2019-04-15'), ('2019-04-13', '2019-04-14'), ('2019-04-19', '2019-04-22'), ('2019-04-19', '2019-04-21'), ('2019-04-20', '2019-04-22'), ('2019-04-20', '2019-04-21'), ('2019-04-26', '2019-04-29'), ('2019-04-26', '2019-04-28'), ('2019-04-27', '2019-04-29'), ('2019-04-27', '2019-04-28'), ('2019-05-03', '2019-05-06'), ('2019-05-03', '2019-05-05'), ('2019-05-04', '2019-05-06'), ('2019-05-04', '2019-05-05'), ('2019-05-10', '2019-05-13'), ('2019-05-10', '2019-05-12'), ('2019-05-11', '2019-05-13'), ('2019-05-11', '2019-05-12'), ('2019-05-17', '2019-05-20'), ('2019-05-17', '2019-05-19'), ('2019-05-18', '2019-05-20'), ('2019-05-18', '2019-05-19'), ('2019-05-24', '2019-05-27'), ('2019-05-24', '2019-05-26'), ('2019-05-25', '2019-05-27'), ('2019-05-25', '2019-05-26'), ('2019-05-31', '2019-06-03'), ('2019-05-31', '2019-06-02'), ('2019-06-01', '2019-06-03'), ('2019-06-01', '2019-06-02'), ('2019-06-07', '2019-06-10'), ('2019-06-07', '2019-06-09'), ('2019-06-08', '2019-06-10'), ('2019-06-08', '2019-06-09'), ('2019-06-14', '2019-06-17'), ('2019-06-14', '2019-06-16'), ('2019-06-15', '2019-06-17'), ('2019-06-15', '2019-06-16'), ('2019-06-21', '2019-06-24'), ('2019-06-21', '2019-06-23'), ('2019-06-22', '2019-06-24'), ('2019-06-22', '2019-06-23'), ('2019-06-28', '2019-07-01'), ('2019-06-28', '2019-06-30'), ('2019-06-29', '2019-07-01'), ('2019-06-29', '2019-06-30'), ('2019-07-05', '2019-07-08'), ('2019-07-05', '2019-07-07'), ('2019-07-06', '2019-07-08'), ('2019-07-06', '2019-07-07'), ('2019-07-12', '2019-07-15'), ('2019-07-12', '2019-07-14'), ('2019-07-13', '2019-07-15'), ('2019-07-13', '2019-07-14'), ('2019-07-19', '2019-07-22'), ('2019-07-19', '2019-07-21'), ('2019-07-20', '2019-07-22'), ('2019-07-20', '2019-07-21'), ('2019-07-26', '2019-07-29'), ('2019-07-26', '2019-07-28'), ('2019-07-27', '2019-07-29'), ('2019-07-27', '2019-07-28'), ('2019-08-02', '2019-08-05'), ('2019-08-02', '2019-08-04'), ('2019-08-03', '2019-08-05'), ('2019-08-03', '2019-08-04'), ('2019-08-09', '2019-08-12'), ('2019-08-09', '2019-08-11'), ('2019-08-10', '2019-08-12'), ('2019-08-10', '2019-08-11'), ('2019-08-16', '2019-08-19'), ('2019-08-16', '2019-08-18'), ('2019-08-17', '2019-08-19'), ('2019-08-17', '2019-08-18'), ('2019-08-23', '2019-08-26'), ('2019-08-23', '2019-08-25'), ('2019-08-24', '2019-08-26'), ('2019-08-24', '2019-08-25'), ('2019-08-30', '2019-09-02'), ('2019-08-30', '2019-09-01'), ('2019-08-31', '2019-09-02'), ('2019-08-31', '2019-09-01'), ('2019-09-06', '2019-09-09'), ('2019-09-06', '2019-09-08'), ('2019-09-07', '2019-09-09'), ('2019-09-07', '2019-09-08'), ('2019-09-13', '2019-09-16'), ('2019-09-13', '2019-09-15'), ('2019-09-14', '2019-09-16'), ('2019-09-14', '2019-09-15'), ('2019-09-20', '2019-09-23'), ('2019-09-20', '2019-09-22'), ('2019-09-21', '2019-09-23'), ('2019-09-21', '2019-09-22'), ('2019-09-27', '2019-09-30'), ('2019-09-27', '2019-09-29'), ('2019-09-28', '2019-09-30'), ('2019-09-28', '2019-09-29'), ('2019-10-04', '2019-10-07'), ('2019-10-04', '2019-10-06'), ('2019-10-05', '2019-10-07'), ('2019-10-05', '2019-10-06'), ('2019-10-11', '2019-10-14'), ('2019-10-11', '2019-10-13'), ('2019-10-12', '2019-10-14'), ('2019-10-12', '2019-10-13'), ('2019-10-18', '2019-10-21'), ('2019-10-18', '2019-10-20'), ('2019-10-19', '2019-10-21'), ('2019-10-19', '2019-10-20'), ('2019-10-25', '2019-10-28'), ('2019-10-25', '2019-10-27'), ('2019-10-26', '2019-10-28'), ('2019-10-26', '2019-10-27'), ('2019-11-01', '2019-11-04'), ('2019-11-01', '2019-11-03'), ('2019-11-02', '2019-11-04'), ('2019-11-02', '2019-11-03'), ('2019-11-08', '2019-11-11'), ('2019-11-08', '2019-11-10'), ('2019-11-09', '2019-11-11'), ('2019-11-09', '2019-11-10'), ('2019-11-15', '2019-11-18'), ('2019-11-15', '2019-11-17'), ('2019-11-16', '2019-11-18'), ('2019-11-16', '2019-11-17'), ('2019-11-22', '2019-11-25'), ('2019-11-22', '2019-11-24'), ('2019-11-23', '2019-11-25'), ('2019-11-23', '2019-11-24'), ('2019-11-29', '2019-12-02'), ('2019-11-29', '2019-12-01'), ('2019-11-30', '2019-12-02'), ('2019-11-30', '2019-12-01'), ('2019-12-06', '2019-12-09'), ('2019-12-06', '2019-12-08'), ('2019-12-07', '2019-12-09'), ('2019-12-07', '2019-12-08'), ('2019-12-13', '2019-12-16'), ('2019-12-13', '2019-12-15'), ('2019-12-14', '2019-12-16'), ('2019-12-14', '2019-12-15'), ('2019-12-20', '2019-12-23'), ('2019-12-20', '2019-12-22'), ('2019-12-21', '2019-12-23'), ('2019-12-21', '2019-12-22')]

may_weekends = [
	('2019-04-27', '2019-05-01'),
	('2019-04-27', '2019-05-02'),
	('2019-04-27', '2019-05-03'),
	('2019-04-27', '2019-05-04'),
	('2019-04-27', '2019-05-05'),
	('2019-04-28', '2019-05-01'),
	('2019-04-28', '2019-05-02'),
	('2019-04-28', '2019-05-03'),
	('2019-04-28', '2019-05-04'),
	('2019-04-28', '2019-05-05'),
	('2019-04-29', '2019-05-02'),
	('2019-04-29', '2019-05-03'),
	('2019-04-29', '2019-05-04'),
	('2019-04-29', '2019-05-05'),
	('2019-04-30', '2019-05-03'),
	('2019-04-30', '2019-05-04'),
	('2019-04-30', '2019-05-05'),
	('2019-05-01', '2019-05-04'),
	('2019-05-01', '2019-05-05')
]

weekday_names = {
    1: 'Пн',
    2: 'Вт',
    3: 'Ср',
    4: 'Чт',
    5: 'Пт',
    6: 'Сб',
    7: 'Вс'
}