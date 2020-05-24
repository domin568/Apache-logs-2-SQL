#!/usr/bin/env python
import sys
import select
import mysql.connector
import re

logdb = mysql.connector.connect(
  host="localhost",
  user="loguser",
  passwd="pass",
  database="logdb"
)

#fw = open ("/home/pi/Stuff/logs.txt","a+") 
#fw2 = open ("/home/pi/Stuff/ApacheLogsToSQL/logsoflogs.txt","a+")
def updateDatabase (args):
	try:
		cursor = logdb.cursor()
    		sqlstatement = """
		INSERT INTO access (ip,identd,userid,date,requestType, resourcePath,protocol,status, bytesReturned, referer, userAgent)
		VALUES('{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}');""".format (args[0],args[1],args[2],args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10])
#		fw2.write (sqlstatement + "\n")
#		fw2.flush ()
		result = cursor.execute (sqlstatement)
		logdb.commit ()
	except mysql.connector.Error as e:
#		fw2.write ("Failed to create table in MySQL: {}".format(e))
#		fw2.flush () 
def parseLine (line):
	l = []
	res = re.search ('^([0-9\.]+) (.+) (.+) \[(.+)\] "([A-Za-z]+) (\S+) (\S+)" (\d+) (\d+) "(\S+)" "(.*)"$', line)
	if res:
		l.append (res.group (1))
		l.append (res.group (2))
		l.append (res.group (3))
                l.append (res.group (4))
                l.append (res.group (5))
                l.append (res.group (6))
                l.append (res.group (7))
                l.append (res.group (8))
                l.append (res.group (9))
                l.append (res.group (10))
                l.append (res.group (11))
		return l
	else:
		pass
#		fw2.write( "NOT PARSED\n" )
#		fw2.flush ()
while 1:
	line = sys.stdin.readline() 
	if line:
		parsed = parseLine (line)
		updateDatabase (parsed)
#		fw.write (line)
#		fw.flush()
	else:
		pass
#		fw2.write ("else1st")
#		fw2.flush()
else:
	pass
#	fw2.write ("else2nd")
#	fw2.close()
#	fw.close()

