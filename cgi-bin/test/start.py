#!/usr/bin/python
import cgi, random, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
name = cgi.escape(form.getvalue('name','Unknown'))
startQuestion = cgi.escape(form.getvalue('q','1'))
randomQuestions = cgi.escape(form.getvalue('r','1'))
word = cgi.escape(form.getvalue('w',''))
# test specific variables
numberOfQuestions = int(open('numberOfQuestions').read().replace('\n',''))
testName = open('testName').read().replace('\n','')

ident = str(random.randint(10000000,99999999))
if (randomQuestions=="1"):
	q = str(random.randint(1,numberOfQuestions))
else:
	q = startQuestion
os.system('date +'+name.replace(' ','\ ')+'\ %b%d > /var/www/darts/tmp/webtest/'+testName+'/'+ident)
os.system('date +%A\ %r >> /var/www/darts/tmp/webtest/'+testName+'/'+ident)
os.system('echo 0000 >> /var/www/darts/tmp/webtest/'+testName+'/'+ident)
#print "Content-type: text/html"
print "Location: test.py?id="+ident+"&q="+q+"&r="+randomQuestions+"&w="+word
#print name+" "+ident
print
