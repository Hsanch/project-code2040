import json
import requests

with requests.Session() as c: 
	url = 'http://challenge.code2040.org/api/register'
	c.get(url)
	#csrftoken = c.cookies['crsftoken']
	register_data = {

		#'csrfmiddlewaretoken' : csrftoken, 
		'token' : '297b6feab3721bf2c68527a718b620f4',
		'github' : 'https://github.com/Hsanch/project-code2040.git'
	}
	json_str = json.dumps(register_data)
	response = c.post(url, data = json_str, headers = { "Referer": "'http://challenge.code2040.org"})
	print response.status_code