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
import socket
import struct
import sys
import ntplib
from time import ctime

TIME1970 = 2208988800L	#thanks to F. Lundh

current = datetime.datetime.now()
currentHours = current.hour * 60 * 60
currentMinutes = current.minute * 60
currentSeconds = current.second
currentTotal = currentHours + currentMinutes + currentSeconds

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send = 'xlb' + 47 * '\0'
server = 'pool.ntp.org'
client.sendto(send, (server, 123))
send, address = client.recvfrom(1024)
if send:
	usend = struct.unpack('!48B', send)
	usend -= TIME1970
	print 'time from server original',usend
	print 'time from server human readable', ctime(usend)

print 'Using the tcp protocol'
print 'retrieved server time original:',send
print 'retrieved server time human readable:',usend
print 'retrieved server time in seconds',total
print 'retrieved time from workstation',current
print 'retrieved time from workstation in seconds',currentTotal
print 'difference between server time and workstation time in seconds',currentTotal - total
