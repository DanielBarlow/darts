#!/usr/bin/python
import cgi, random, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
pswd = cgi.escape(form.getvalue('pswd','none'))
name = cgi.escape(form.getvalue('name','none'))

# test specific variables
testName = open('testName').read().replace('\n','')

print "Content-type: text/html"
print

if (pswd == "Password3"):
	os.system("/home/www/ccst/bin/"+testName.replace('/','')+"listname | grep -i \""+name+"\" | sort > /home/www/ccst/tmp/webtest/"+testName+"/listname")
	f = open('/home/www/ccst/tmp/webtest/'+testName+'/listname')
	last=""
	for n in f:
		n=n.replace('\n','')
		if (last != n):
			print "<b>"+n+"</b><br>did "
			# put score sheets in file
			os.system(testName.replace('/','')+"namescore "+n+" > /home/www/ccst/tmp/webtest/"+testName+"/score")
			# count number of right and wrong (questions answered)
			os.system("echo \"`cat /home/www/ccst/tmp/webtest/"+testName+"/score | grep -c wrong`+`cat /home/www/ccst/tmp/webtest/"+testName+"/score | grep -c right`\" | bc -l > /home/www/ccst/tmp/webtest/"+testName+"/number")
			# calculate percentage right
			os.system("echo \"`cat /home/www/ccst/tmp/webtest/"+testName+"/score | grep -c right`/(`cat /home/www/ccst/tmp/webtest/"+testName+"/score | grep -c wrong`+`cat /home/www/ccst/tmp/webtest/"+testName+"/score | grep -c right`)*100\" | bc -l > /home/www/ccst/tmp/webtest/"+testName+"/grade")
			nf = open('/home/www/ccst/tmp/webtest/'+testName+'/number')
			print nf.read()+" questions and "
			gf = open('/home/www/ccst/tmp/webtest/'+testName+'/grade')
			print gf.read().replace('\n','')+"% were correct."
			print "<br>"
			last=n
else:
	print "Access Denied"
