#!/usr/bin/env python
#author Peter Adamson 3319005
#References used:

#to parse the time from workstation into a readable format
#https://stackoverflow.com/questions/35375148/python-error-attributeerror-datetime-datetime-object-has-no-attribute-split

#information on split
#http://www.pythonforbeginners.com/dictionary/python-split

#information on ntplib
#https://stackoverflow.com/questions/12664295/ntp-client-in-python
#and
#https://pypi.python.org/pypi/ntplib/

import datetime
import ntplib
from time import ctime

current = datetime.datetime.now()
currentHours = current.hour * 60 * 60
currentMinutes = current.minute * 60
currentSeconds = current.second
currentTotal = currentHours + currentMinutes + currentSeconds

client = ntplib.NTPClient()
response = client.request('time-a.nist.gov')
human = ctime(response.tx_time)
split = human.split(" ")
time = split[3].split(":")
hours = int(time[0]) * 60 * 60
minutes = int(time[1]) * 60
seconds = int(time[2])
total = hours + minutes + seconds
print 'Using the tcp protocol'
print 'retrieved server time original:',response
print 'retrieved server time human readable:',human
print 'retrieved server time in seconds',total
print 'retrieved time from workstation',current
print 'retrieved time from workstation in seconds',currentTotal
print 'difference between server time and workstation time in seconds',currentTotal - total
