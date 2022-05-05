# -*- coding: utf-8 -*-
# @Author  : Lison Song
# @Time    : 2022/5/5 12:56
import json

if __name__ == '__main__':
    load_dict = {}
    with open("city_code.json", 'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
    # print(load_dict)
    # print(load_dict['城市代码'])
    province_list = []
    city_list = []
    for province in load_dict['城市代码']:
        print(province)
        province_list.append(province['省'])
        if province['省'] == '江苏':
            print(province['市'])
            for city in province['市']:
                city_list.append(city['市名'])

    print(province_list)
    print(city_list)