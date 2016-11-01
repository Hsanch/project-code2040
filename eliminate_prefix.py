import json
import requests

def eliminate_prefix(Prefix, Array):
	index = 0
	temp_ary = Array
	temp_ary2 = []
	while index < len(temp_ary):
		if temp_ary[index].find(Prefix) != -1:
			temp_ary2 temp_ary[index]
			index+=1
		else:
			index+=1

	print temp_ary2
	return temp_ary2


with requests.Session() as c: 
	url = 'http://challenge.code2040.org/api/prefix'
	
	prefix_data = {
		
		'token' : '297b6feab3721bf2c68527a718b620f4'
	}

	response = c.post(url, data = prefix_data, headers = { "eferer": "http://challenge.code2040.org"})
	content = json.loads(response.content)


prefix = content['prefix']
array = content['array']

new_array = eliminate_prefix(prefix, array)


with requests.Session() as j: 

	url = 'http://challenge.code2040.org/api/prefix/validate'

	new_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'array' : new_array
	}

	response2 = j.post(url, data = new_data, headers = {"Referer" : "http://challenge.code2040.org"})

print response2
print new_data