# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/2 23:23
Author: Lison Song
"""
import os

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_INPUTS = os.path.join(DATA_DIR, "input")
DATA_OUTPUTS = os.path.join(DATA_DIR, 'output')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DATA_INPUTS, exist_ok=True)
os.makedirs(DATA_OUTPUTS, exist_ok=True)

if __name__ == '__main__':
    print(DATA_INPUTS, DATA_OUTPUTS)