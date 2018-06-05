# Copyright (c) 2018 GenYuanLian
# -*- coding: utf-8 -*-


def _init():  # 初始化
    global _global_dict  # 矿池参数
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, defvalue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defvalue


subsidy_cal_check = {}
subsidy_cal = {}  # 算力补贴表
total_cal = 1
total_cal_cache=0
time_check = 0  # time check per day
time_check_share = True  # time check per share


def reset_subsidy():
    for key in subsidy_cal:
        if subsidy_cal[key] == 0:
            del subsidy_cal[key]
        else:
            subsidy_cal[key] = 0
    global total_cal_cache, time_check_share
    total_cal_cache = 0
    time_check_share=False
