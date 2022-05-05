# -*- coding: utf-8 -*-
# @Author  : Lison Song
# @Time    : 2022/5/5 11:45

import sys
import weather
from PyQt5.QtWidgets import QApplication, QDialog
import requests
import pandas as pd


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = weather.Ui_weather()
        self.ui.setupUi(self)

    def queryWeather(self):
        cityName = self.ui.comboBox_select_city.currentText()
        # cityCode = self.getCode(cityName)
        cityCode = self.search_city_code(cityName)
        r = requests.get("http://t.weather.sojson.com/api/weather/city/{}".format(cityCode))

        print(r.json())

        if r.json().get('status') == 200:
            weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
                r.json()['cityInfo']['city'],
                r.json()['data']['forecast'][0]['ymd'],
                r.json()['data']['forecast'][0]['type'],
                int(r.json()['data']['pm25']),
                r.json()['data']['quality'],
                r.json()['data']['wendu'],
                r.json()['data']['shidu'],
                r.json()['data']['forecast'][0]['fl'],
                r.json()['data']['forecast'][0]['notice'],
            )
        else:
            weatherMsg = '天气查询失败，请稍后再试！'

        self.ui.textEdit_result.setText(weatherMsg)

    def getCode(self, cityName):
        cityDict = {"北京": "101010100",
                    "上海": "101020100",
                    "天津": "101030100",
                    "徐州": "101190801",
                    "乌鲁木齐": "101130101"}

        return cityDict.get(cityName)

    def search_city_code(self, city_name):
        # print(city_name)
        city_code = '-1'
        try:
            df = pd.read_json('city_code.json')
            for row in df.values:
                # print(row)
                row_data = row[0]
                city_data = row_data['市']
                for cd in city_data:
                    # print(cd['市名'], cd['编码'])
                    if (city_name == cd['市名'] or cd['市名'] in city_name):
                        city_code = cd['编码']
                        break
        except Exception as e:
            print(f" ERROR: {e}")

        print(city_code)
        return city_code

    def clearText(self):
        self.ui.textEdit_result.clear()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
