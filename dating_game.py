import json 
import requests
import isodate
import datetime

def add_months(totalMonths, months_added, Added_Years):
	temp = totalMonths + months_added
	if (temp) <= 30:
		totalMonths += months_added
		return totalMonths
	else:
		Added_Years+=1
		totalMonths = temp
		totalMonths = totalMonths - 30 
		add_months(totalMonths,0,Added_Years)
		return totalMonths


def add_days(totalDays, days_added, Added_Months):
	temp = totalDays + days_added
	if (temp) <= 30:
		totalDays += days_added
		return totalDays
	else:
		Added_Months+=1
		totalDays = temp
		totalDays = totalDays - 30 
		add_days(totalDays,0,Added_Months)
		return totalDays



def add_hours(totalHours, hours_added, Added_Days):
	temp = totalHours + hours_added
	if (temp) < 24:
		totalHours += hours_added
		return totalHours
	else:
		Added_Days+=1
		totalHours = temp
		totalHours = totalHours - 24 
		add_hours(totalHours,0,Added_Days)
		return totalHours



def add_minutes(totalMinutes, Minutes_added, Added_Hours):
	temp = totalMinutes + Minutes_added
	if (temp) < 60:
		totalMinutes += Minutes_added
		return totalMinutes
	else:
		Added_Hours+=1
		totalMinutes = temp
		totalMinutes = totalMinutes - 60 
		add_minutes(totalMinutes,0,Added_Hours)
		return totalMinutes



def add_seconds(totalSeconds, seconds_added, Added_Minutes):
	temp = totalSeconds + seconds_added
	if (temp) < 60:
		totalSeconds += seconds_added
		return totalSeconds
	else:
		Added_Minutes+=1
		totalSeconds = temp
		totalSeconds = totalSeconds - 60 
		add_seconds(totalSeconds,0,Added_Minutes)
		return totalSeconds



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

print datestamp
print interval

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
totalSeconds = datestamp.second
totalMinutes = datestamp.minute
totalHours = datestamp.hour
totalDays = datestamp.day
totalMonths = datestamp.month
totalYears = datestamp.year

leftover_minutes = 0
leftover_hours = 0
leftover_days = 0
leftover_months = 0
leftover_years = 0

totalSeconds = add_seconds(totalSeconds,seconds_added,leftover_minutes)
minutes_added = leftover_minutes + minutes_added

totalMinutes = add_minutes(totalMinutes,minutes_added,leftover_hours)
hours_added = leftover_hours + hours_added

totalHours = add_hours(totalHours,hours_added,leftover_days)
days_added = leftover_days + days_added

totalDays = add_days(totalDays,days_added,leftover_months)
months_added = leftover_months + months_added

totalMonths = add_months(totalMonths,months_added,leftover_years)

totalYears = totalYears + leftover_years

datestamp = datestamp.replace(year = totalYears,month = totalMonths, day = totalDays,hour = totalHours, minute = totalMinutes, second = totalSeconds)

print datestamp

datestamp = isodate.datetime_isoformat(datestamp)

print datestamp

with requests.Session() as j:

	validate_url = 'http://challenge.code2040.org/api/dating/validate'

	new_data = {

		'token' : '297b6feab3721bf2c68527a718b620f4',
		'datestamp' : datestamp

	}

	headers = { 'Content-Type' : 'application/json'}


	response2 = j.post(url = validate_url, json = new_data, headers = headers )

print response2
