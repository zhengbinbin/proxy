#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:郑彬彬
# @date: 2019/11/25 9:35
# github:https://github.com/zhengbinbin

import urllib, time, commands, os

url = 'http://project-databus.gsdata.cn:9999'
time_now = time.strftime('%Y-%m-%d %H:%M:%S')
def get_code():
    flag = 0
    for i in range(0,5):
        code = urllib.urlopen(url).code
        if code != 200:
            flag += 1
        time.sleep(20)
    if flag == 5:
        with open('/mnt/check_project.log','a') as f:
            f.write(time_now + ': 连续5次检测databus状态异常，将重启php\n')
            result = commands.getstatusoutput('service php-fpm restart')
            if result[0] == 0:
                f.write(time_now + ': php已重启。。。\n')
            else:
                f.write(time_now + ': php重启异常！！！\n')

if __name__ == '__main__':
    get_code()