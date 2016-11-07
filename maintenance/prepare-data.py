#!/usr/bin/env python

import os

# data obtained from https://www.meteoblue.com/en/weather/archive/yearcomparison/troms%C3%B8_norway_3133895?daterange=2016-10-28+to+2016-11-04&compare_years=&compare_years%5B%5D=2016&compare_years%5B%5D=2015&compare_years%5B%5D=2014&compare_years%5B%5D=2013&params=&params%5B%5D=11%3B2+m+above+gnd&cumulate=0&utc_offset=1&aggregation=hourly&temperatureunit=CELSIUS&windspeedunit=KILOMETER_PER_HOUR&degree_day_type=10%3B30&degree_day_base=10&degree_day_limit=30

# Year;Month;Day;Hour;Minute;Temperature 2016  [2 m above gnd];Temperature 2015  [2 m above gnd];Temperature 2014  [2 m above gnd];Temperature 2013  [2 m above gnd]

d_month = {'10': 'oct', '11': 'nov'}

with open('history_export_2016-11-04T08-34-52.csv', 'r') as f:
    for line in f:
        l = line.strip('\n').split(';')
        t = {}
        _, month, day, hour, minute, t[2016], t[2015], t[2014], t[2013] = tuple(l)
        for y in [2013, 2014, 2015, 2016]:
            path = 'data/{0}/{1}'.format(y, d_month[month])
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, day), 'a') as data_f:
                time_stamp = '{0}:{1}'.format(hour, minute)
                temperature = t[y]
                data_f.write('{0} {1}\n'.format(time_stamp, temperature))
