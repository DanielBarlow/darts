#!/usr/bin/python
import cgi, random, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
pswd = cgi.escape(form.getvalue('pswd','none'))
name = cgi.escape(form.getvalue('name','none')).replace('\n','')

# test specific variables
testName = open('testName').read().replace('\n','')

print "Content-type: text/html"
print

if (pswd == "Password3"):
	print "Score report for "+name+".<p>"
	os.system("echo \"`/home/www/ccst/bin/"+testName.replace('/','')+"namescore "+name+" | grep right | wc -l`/(`/home/www/ccst/bin/"+testName.replace('/','')+"namescore "+name+" | grep wrong | wc -l`+`/home/www/ccst/bin/"+testName.replace('/','')+"namescore "+name+" | grep right | wc -l`+`/home/www/ccst/bin/"+testName.replace('/','')+"namescore "+name+" | grep unanswered | wc -l`)*100\" | bc -l > /home/www/ccst/tmp/webtest/"+testName+"/grade")
	gf = open('/home/www/ccst/tmp/webtest/'+testName+'/grade')
	print gf.read().replace("\n","<br>")
	os.system("/home/www/ccst/bin/"+testName.replace('/','')+"namescore "+name+" > /home/www/ccst/tmp/webtest/"+testName+"/score")
	sf = open('/home/www/ccst/tmp/webtest/'+testName+'/score')
	print sf.read().replace("\n","<br>").replace('right','<u><font color=green>right</font></u>').replace('wrong','<u><font color=red>wrong</font></u>').replace('unanswered','<u><font color=gray>unanswered</font></u>')
	
else:
	print "Access Denied"
