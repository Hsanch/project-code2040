import json 
import requests

def find_needle(NEEDLE, HAYSTACK):
	INDEX = 0
	while INDEX < len(haystack):
		if haystack[INDEX] == needle:
			return INDEX
		else:
			INDEX+=1

with requests.Session() as c: 

	url = 'http://challenge.code2040.org/api/haystack'

	haystack_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4'
	}
	headers = {'Content-Type' : 'application/json'}

	response = c.post(url, data = json.dumps(haystack_data), headers = headers)

	content = json.loads(response.content)


needle = content['needle']
haystack = content['haystack']

index = find_needle(needle,haystack)


with requests.Session() as j: 

	url = 'http://challenge.code2040.org/api/haystack/validate'

	needle_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'needle' : index
	}

	headers = { 'Content-Type' : 'application/json'}

	response = j.post(url, data = json.dumps(needle_data), headers = headers)

print response.status_code