# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/2 23:23
Author: Lison Song
"""
import os

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
DATA_DIR = os.path.join(BASE_DIR, "data")
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(DATA_DIR, "input")
SAMPLE_OUTPUTS = os.path.join(DATA_DIR, 'output')

if __name__ == '__main__':
    print(SAMPLE_DIR, SAMPLE_INPUTS, SAMPLE_OUTPUTS)