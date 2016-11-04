import json
import requests

def eliminate_prefix(Prefix, Array):
	index= 0
	while index < len(Array):
		tempString = Array[index]
		if tempString.find(Prefix) != -1:
			Array.remove(Array[index])
		else:
			index+=1
	return Array

def eliminate_prefix2(Prefix, Array):
	index = 0
	temp_ary = Array
	while index < len(temp_ary):
		if temp_ary[index].find(Prefix) != -1:
			temp_ary.remove(temp_ary[index])
			index+=1
		else:
			index+=1
	return temp_ary


with requests.Session() as c: 
	url = 'http://challenge.code2040.org/api/prefix'
	
	prefix_data = {
		
		'token':'297b6feab3721bf2c68527a718b620f4'
	}

	headers = { 'Content-Type' : 'application/json'}

	response = c.post(url, data = json.dumps(prefix_data), headers = headers)
	print response.content

content = json.loads(response.content)
print content

prefix = content['prefix']
array = content['array']



array =  eliminate_prefix(prefix,array)

with requests.Session() as j: 

	array = eliminate_prefix(prefix,array)
	#array = json.dumps(array)

	token = '297b6feab3721bf2c68527a718b620f4'
	#token = json.dumps(token)

	url = 'http://challenge.code2040.org/api/prefix/validate'

	new_data = {

		'token': token,
		'array': array
	}
	headers = {'Content-Type' : 'application/json'}
	response2 = j.post(url, json = new_data, headers = headers)


print "\n\n"
print response2
print new_data