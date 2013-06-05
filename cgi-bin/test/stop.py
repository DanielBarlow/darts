#!/usr/bin/python
import cgi, random, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
ident = cgi.escape(form.getvalue('id',''))
# test specific variables
testName = open('testName').read().replace('\n','')

# get results
f = open('/var/www/darts/tmp/webtest/'+testName+'/'+ident)
results = f.read()
print "Content-type: text/html"
# print results
print 
# count number of right and wrong (questions answered)
os.system("echo \"`cat /var/www/darts/tmp/webtest/"+testName+"/"+ident+" | grep -c wrong`+`cat /var/www/darts/tmp/webtest/"+testName+"/"+ident+" | grep -c right`\" | bc -l > /var/www/darts/tmp/webtest/"+testName+"/number")
# calculate percentage right
os.system("echo \"`cat /var/www/darts/tmp/webtest/"+testName+"/"+ident+" | grep -c right`/(`cat /var/www/darts/tmp/webtest/"+testName+"/"+ident+" | grep -c wrong`+`cat /var/www/darts/tmp/webtest/"+testName+"/"+ident+" | grep -c right`)*100\" | bc -l > /var/www/darts/tmp/webtest/"+testName+"/grade")
nf = open('/var/www/darts/tmp/webtest/'+testName+'/number')
gf = open('/var/www/darts/tmp/webtest/'+testName+'/grade')
percent = gf.read().replace('\n','')

if (testName=="aplus/701" or testName=="aplus/701b" or testName=="aplus/701c" or testName=="aplus/701d" or testName=="aplus/801a"):
	minscore = 675
if (testName=="aplus/702" or testName=="aplus/702b" or testName=="aplus/702c" or testName=="aplus/702d" or testName=="aplus/802a"):
	minscore = 700
if (testName=="netplus" or testName=="netplus/005a"):
	minscore = 720
if (testName=="serverplus"):
	minscore = 750

score = int(float('0'+percent)*8+100)
print "Passing Score: "+str(minscore)+"<br>"
print "Your Score: "+str(score)+"<br>"
if (minscore<=score):
	print "<font color=green size=8>PASS</font><p>"
else:
	print "<font color=red size=8>FAIL</font><p>"
print nf.read()+" questions and "
print percent+"% were correct.<p>"
print results.replace('0000\nunanswered','\n<br>').replace('right','<font color=green>right</font><br>').replace('wrong','<font color=red>wrong</font><br>').replace('unanswered','<font color=gray>unanswered</font><br>')
print "<a href=/>Go Home.</a>"
