import json 
import requests

def find_needle(NEEDLE, HAYSTACK):
	INDEX = 0
	while INDEX < len(haystack):
		if haystack[INDEX] == needle:
			return INDEX
		else:
			INDEX+=1

def load_haystack(Content):
	i = 0
	temp = ''
	temp_haystack = []
	while Content[i] != '[':
		i+=1
	i+=2
	while Content[i] != ']':
		if Content[i] != '"':
			temp += Content[i]
			i+=1
		else:
			i+=1

	temp_haystack = temp.split(',')

	return temp_haystack




def get_needle(Content):
	temp_needle = ''
	i = 0
	while content[i] != ':':
		i+=1

	i+=2
	while content[i] != '"':
		temp_needle += content[i]
		i+=1
	return temp_needle

with requests.Session() as c: 

	url = 'http://challenge.code2040.org/api/haystack'

	haystack_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4'
	}

	response = c.post(url, data = haystack_data, headers = {"Referer" : "http://challenge.code2040.org"})

	content = response.content


needle = get_needle(content)
haystack = load_haystack(content)
index = find_needle(needle,haystack)


with requests.Session() as j: 

	url = 'http://challenge.code2040.org/api/haystack'

	needle_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'needle' : index
	}

	response = j.post(url, data = haystack_data, headers = {"Referer" : "http://challenge.code2040.org"})

print response.status_code
