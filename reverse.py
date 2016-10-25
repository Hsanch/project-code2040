import json
import requests


def reverse1(string):
	revString = string[::-1]
	return revString

def reverse2(string):
	temp_string = ''
	i = len(string)

	while i > 0:
		temp_string += string[i-1]
		i -= 1
	return temp_string



with requests.Session() as c: 

	url = 'http://challenge.code2040.org/api/reverse'

	DATA = {

		'token' : '297b6feab3721bf2c68527a718b620f4'
	}

	response = c.post(url, data = DATA, headers = { "Referer": "http://challenge.code2040.org"})
	
	keyword = response.content
	result = reverse2(keyword)

	validateURL = 'http://challenge.code2040.org/api/reverse/validate'
	reversedString = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'string' : result
	}

	response2 = c.post(validateURL, data = reversedString, headers = {"Referer": "http://challenge.code2040.org"})
	print response2.status_code
	print keyword
	print reverse2(keyword)
