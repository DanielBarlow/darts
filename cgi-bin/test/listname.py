#!/usr/bin/python
import cgi, random, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
pswd = cgi.escape(form.getvalue('pswd','none'))
name = cgi.escape(form.getvalue('name','all'))

# test specific variables
testName = open('testName').read().replace('\n','')

print "Content-type: text/html"
print

if (pswd == "Password3"):
	print "<form target=_blank action=/cgi-bin/"+testName+"/gradeall.py method=post><input name=pswd type=hidden value="+pswd+"><input type=hidden name=name value="+name+"><input type=submit value=\"Grade All\"></form><form target=_blank action=/cgi-bin/"+testName+"/getscore.py method=post><input name=pswd type=hidden value="+pswd+"><input type=submit name=name value=\""
	if (name == "all"):
		os.system("head -n1 -q /home/www/ccst/tmp/webtest/"+testName+"/[0-9]* | sort > /home/www/ccst/tmp/webtest/"+testName+"/listname")
	else:
		os.system("head -n1 -q /home/www/ccst/tmp/webtest/"+testName+"/[0-9]* | grep -i \""+name+"\" | sort > /home/www/ccst/tmp/webtest/"+testName+"/listname")
	f = open('/home/www/ccst/tmp/webtest/'+testName+'/listname')
	print f.read().replace("\n","\"><br><input type=submit name=name value=\"")
	print "\"></form>"
else:
	print "Access Denied"
