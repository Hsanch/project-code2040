import json
import requests

def eliminate_prefix(Prefix, Array):
	index = 0
	temp_ary = Array
	temp_ary2 = []
	while index < len(temp_ary):
		if temp_ary[index].find(Prefix) != -1:
			temp_ary.remove(temp_ary[index])
		else:
			index+=1
	temp_ary2 = temp_ary
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

print content


new_array = eliminate_prefix(prefix, array)

with requests.Session() as j: 
	URL = 'http://challenge.code2040.org/api/prefix/validate'

	validate_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'array' : new_array
	}

	validate_data = json.dumps(validate_data)

	response2 = j.post(URL, data = validate_data, headers = { "Referer": "http://challenge.code2040.org"})

print response2
print "\n"
print new_array
print '\n'
print validate_data