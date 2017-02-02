import json 
import requests
import isodate
import datetime

with requests.Session() as c:
	url_dating = 'http://challenge.code2040.org/api/dating'

	receiving_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4'

	}

	headers = { 'Content-Type' : 'application/json'}

	response = c.post(url_dating, json = receiving_data, headers = headers)
	content = json.loads(response.content)


interval =  content['interval']

datestamp = content['datestamp']

datestamp = isodate.parse_datetime(datestamp)
time_zone = datestamp.tzinfo

months_added = 0


days_added = interval/86400
day_remainder = interval%86400

hours_added = day_remainder/3600
hour_remainder = day_remainder%3600

minutes_added = hour_remainder/60
minute_remainder = hour_remainder%60

seconds_added = minute_remainder

#assign data form the iso 8601 to these variables
InitialSeconds = datestamp.second
InitialMinutes = datestamp.minute
InitialHours = datestamp.hour
InitialDays = datestamp.day
InitialMonths = datestamp.month
InitialYears = datestamp.year


if(InitialSeconds + seconds_added >= 60):
	totalSeconds = (InitialSeconds + seconds_added) - 60
	LeftOver = 1
else:
	totalSeconds = InitialSeconds + seconds_added
	LeftOver = 0


if(InitialMinutes + minutes_added + LeftOver >= 60):
	totalMinutes = (InitialMinutes + minutes_added + LeftOver) - 60
	LeftOver = 1
else:
	totalMinutes = InitialMinutes + minutes_added + LeftOver
	LeftOver = 0

if(InitialHours + hours_added + LeftOver >= 24):
	totalHours = (InitialHours + hours_added + LeftOver) - 24
	LeftOver = 1
else:
	totalHours = InitialHours + hours_added + LeftOver
	LeftOver = 0

#ADD DAYS HERE::::::

if(InitialDays + days_added + LeftOver > 30):
	totalDays = (InitialDays + days_added + LeftOver) - 30
	LeftOver = 1
else:
	totalDays = InitialDays + days_added + LeftOver
	LeftOver = 0

if(LeftOver == 1):
	if(InitialMonths +  LeftOver > 12):
		totalMonths = (InitialMonths + LeftOver) - 12
		LeftOver = 1
	else:
		totalMonths = InitialMonths + LeftOver
		LeftOver = 0
else:
	totalMonths = InitialMonths


totalYears = InitialYears + LeftOver


datestamp = datestamp.replace(year = totalYears,month = totalMonths, day = totalDays,hour = totalHours, minute = totalMinutes, second = totalSeconds)


datestamp = isodate.datetime_isoformat(datestamp)

with requests.Session() as j:

	validate_url = 'http://challenge.code2040.org/api/dating/validate'

	new_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'datestamp' : datestamp

	}

	headers = { 'Content-Type' : 'application/json'}


	response2 = j.post(url = validate_url, json = new_data, headers = headers )


print response2
