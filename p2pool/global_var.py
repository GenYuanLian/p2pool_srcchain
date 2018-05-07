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


subsidy_cal = {}  # 算力补贴表
total_cal = 1
time_check=0

# def pulse_one():
#     for key in subsidy_cal:
#         subsidy_cal[key] = subsidy_cal[key] + 1
#     global total_cal
#     total_cal = total_cal + len(subsidy_cal)


def reset_subsidy():
    for key in subsidy_cal:
        subsidy_cal[key] = 0
    global total_cal
    total_cal = 0
