import json
import requests


def get_array(Content):
	i = 0
	temp = ''
	temp_array = []
	while Content[i] != '[':
		i+=1
	i+=2
	while Content[i] != ']':
		if Content[i] != '"':
			temp += Content[i]
			i+=1
		else:
			i+=1

	temp_array = temp.split(',')

	return temp_array


def get_prefix(Content):
	temp_prefix = ''
	i = 0
	while content[i] != ':':
		i+=1

	i+=2
	while content[i] != '"':
		temp_prefix += content[i]
		i+=1
	return temp_prefix


with requests.Session() as c: 
	url = 'http://challenge.code2040.org/api/prefix'
	
	prefix_data = {
		
		'token' : '297b6feab3721bf2c68527a718b620f4'
	}

	response = c.post(url, data = prefix_data, headers = { "eferer": "http://challenge.code2040.org"})

content = response.content
array = []
prefix = get_prefix(content)
array = get_array(content)
new_array = []
new_array=[]

index = 0
temp = ""

print "CONTENT " 
print content

print "ARRAY "
print array
while index < len(array):
	if array[index].find(prefix) != -1:
		array.remove(array[index])
	else:
		index+=1

print "PREFIX " 
print prefix
print "NEW ARRAY " 
print array

#print new_array