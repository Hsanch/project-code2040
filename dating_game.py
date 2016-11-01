import json 
import requests 

with requests.Session() as c:
	url_dating = 'http://challenge.code2040.org/api/dating'

	receiving_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4'

	}

	response = c.post(url_dating, data = receiving_data, headers = {"Referer" : "http://challenge.code2040.org"})
	content = json.loads(response.content)


interval =  content['interval']

datestamp = content['datestamp']
datestamp = iso8601.parse_date(datestamp)

print datestamp
print interval

days = interval/86400
day_remainder = interval%86400

hours = day_remainder/3600
hour_remainder = day_remainder%3600

minutes = hour_remainder/60
minute_remainder = hour_remainder%60

print days
print day_remainder
print hours
print hour_remainder
print minutes
print minute_remainder



Year = datestamp[1]
print 