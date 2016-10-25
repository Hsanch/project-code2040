import json
import requests

with requests.Session() as c: 
	url = 'http://challenge.code2040.org/api/register'
	
	register_data = {
		
		'token' : '297b6feab3721bf2c68527a718b620f4',
		'github' : 'https://github.com/Hsanch/project-code2040.git'
	}
	response = c.post(url, data = register_data, headers = { "Referer": "http://challenge.code2040.org"})
	print response.status_code