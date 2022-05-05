# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/5 18:46
Author: Lison Song
"""
import json
from conf import CITY_CODE_FILE


def get_city_by_province(province_name):
    city_list = []
    if province_name == '请选择':
        return city_list
    else:
        with open(CITY_CODE_FILE, 'r', encoding='UTF-8') as f:
            load_dict = json.load(f)
        for province in load_dict['城市代码']:
            if province['省'] == province_name:
                # print(province['市'])
                for city in province['市']:
                    city_list.append(city['市名'])
                break
    return city_list



if __name__ == '__main__':
    print(get_city_by_province("江苏"))
    # load_dict = {}
    # with open("city_code.json", 'r', encoding='UTF-8') as f:
    #     load_dict = json.load(f)
    # # print(load_dict)
    # # print(load_dict['城市代码'])
    # province_list = []
    # city_list = []
    # for province in load_dict['城市代码']:
    #     print(province)
    #     province_list.append(province['省'])
    #     if province['省'] == '江苏':
    #         print(province['市'])
    #         for city in province['市']:
    #             city_list.append(city['市名'])
    #
    # print(province_list)
    # print(city_list)

