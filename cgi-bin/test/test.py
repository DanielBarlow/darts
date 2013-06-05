#!/usr/bin/python
import cgi, random, os, time
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
ident = cgi.escape(form.getvalue('id',''))
number = cgi.escape(form.getvalue('n','0'))
forceQuestion = cgi.escape(form.getvalue('q','all'))
randomQuestions = cgi.escape(form.getvalue('r','1'))
wordMatch = cgi.escape(form.getvalue('w',' '))
randomfoo = random.SystemRandom()

# test specific variables
numberOfQuestions = int(open('numberOfQuestions').read().replace('\n',''))
testName = open('testName').read().replace('\n','')


# other variables
f = open('/var/www/darts/cgi-bin/'+testName+'/onlyquestions')
questions = f.read()
myans = ""
repeat = 0
right = 0
wrong = 0
stop = 0
q = 1
print "Content-type: text/html"
print

# checkAns,genRand,dispQues 



# checkAns

#get the number of and their answer for the last question
#get number of last question
os.system("rm -f /var/www/darts/tmp/webtest/"+testName+"/lastq"+ident)
os.system("sleep 0.025")
os.system("tail -n 1 /var/www/darts/tmp/webtest/"+testName+"/"+ident+" > /var/www/darts/tmp/webtest/"+testName+"/lastq"+ident)
os.system("sleep 0.05")
qf = open('/var/www/darts/tmp/webtest/'+testName+'/lastq'+ident)
q = qf.read()
#put the last right answer in answer+ident
os.system("rm -f /var/www/darts/tmp/webtest/"+testName+"/answer"+str(ident))
os.system("sleep 0.025")
os.system("awk 'NR=="+str(q)+"' /var/www/darts/cgi-bin/"+testName+"/onlyanswers > /var/www/darts/tmp/webtest/"+testName+"/answer"+str(ident))
os.system("sleep 0.05")
#open right answer
af = open('/var/www/darts/tmp/webtest/'+testName+'/answer'+ident)
#get and clean up the right answer
corans = af.read().replace("\n0","").replace("\n","")
#os.system("test "+corans+" `tail -n 1 /var/www/darts/tmp/webtest/"+testName+"/"+ident+"` > /var/www/darts/tmp/webtest/"+testName+"/right"+ident)
#get their answer
a = cgi.escape(form.getvalue('a','')).upper()
b = cgi.escape(form.getvalue('b','')).upper()
c = cgi.escape(form.getvalue('c','')).upper()
d = cgi.escape(form.getvalue('d','')).upper()
e = cgi.escape(form.getvalue('e','')).upper()
f = cgi.escape(form.getvalue('f','')).upper()
g = cgi.escape(form.getvalue('g','')).upper()
myans = ""
a1="N0Noccuranc3"
a2="N0Noccuranc3"
a3="N0Noccuranc3"
a4="N0Noccuranc3"
a5="N0Noccuranc3"
a6="N0Noccuranc3"
a7="N0Noccuranc3"
if (a=="ON"):
	myans = "A,"
	a1="A. "
if (b=="ON"):
	myans = myans+"B,"
	a2="B. "
if (c=="ON"):
	myans = myans+"C,"
	a3="C. "
if (d=="ON"):
	myans = myans+"D,"
	a4="D. "
if (e=="ON"):
	myans = myans+"E,"
	a5="E. "
if (f=="ON"):
	myans = myans+"F,"
	a6="F. "
if (g=="ON"):
	myans = myans+"G,"
	a6="G. "
myans = myans[0:len(myans)-1]
#html code
print "<html><head><title>DARTS - Daniel's Advanced Readiness Testing System</title><style> html,body {padding:0;margin:0;} div.content {padding:10px;} </style>"
#analytics
f = open('/var/www/darts/www/analytics.html')
analyticsCode = f.read()
print analyticsCode
#display logo, ad, then last question
print "</head><body><center><img src=\"/darts.png\"></center><div class=content><center>"
f = open('/var/www/darts/www/adsense1.html')
adsenseAd = f.read()
print adsenseAd
print "</center>"
print questions[questions.find('QUESTION NO: '+str(int(q))):questions.find('QUESTION NO: '+str(int(q)+1))].replace(a1,"<br><b>"+a1+"</b>").replace(a2,"<br><b>"+a2+"</b>").replace(a3,"<br><b>"+a3+"</b>").replace(a4,"<br><b>"+a4+"</b>").replace(a5,"<br><b>"+a5+"</b>").replace(a6,"<br><b>"+a6+"</b>").replace('\nA. ','<p>A. ').replace('\nB. ','<br>B. ').replace('\nC. ','<br>C. ').replace('\nD. ','<br>D. ').replace('\nE. ','<br>E. ').replace('\nF. ','<br>F. ').replace('\nG. ','<br>G. ')
print "<br>"
#test if their last answer was right

if (myans==""):
	print "I didn't see an answer for the last question. Did you just start?"
	if (cgi.escape(os.environ["HTTP_USER_AGENT"])!="Mediapartners-Google"):
		os.system('echo unanswered >> /var/www/darts/tmp/webtest/'+testName+'/'+ident)
elif (myans == corans):
	print "<h3>Correct, the answer was "+corans+"\n</h3>"
	if (cgi.escape(os.environ["HTTP_USER_AGENT"])!="Mediapartners-Google"):
		os.system('echo right >> /var/www/darts/tmp/webtest/'+testName+'/'+ident)
else:
	print "<h3>Nope, the answer was "+corans+"\n</h3>"
	if (cgi.escape(os.environ["HTTP_USER_AGENT"])!="Mediapartners-Google"):
		os.system('echo wrong >> /var/www/darts/tmp/webtest/'+testName+'/'+ident)
# genRand
if (forceQuestion=="all"):
	newq = randomfoo.randint(1,numberOfQuestions)
else:
	newq = int(forceQuestion)
q = newq
nextq = "all"

question = questions[questions.find('QUESTION NO: '+str(q)):questions.find('QUESTION NO: '+str(q+1))]

if (wordMatch!=" "):
	for i in range(numberOfQuestions):
		testQ = q+i+1
		if (testQ>numberOfQuestions):
			testQ = testQ-numberOfQuestions
		if (numberOfQuestions==(i+1)):
			question = "<b>Could not find any questions with "+wordMatch+"</b>"
			break
		else:
			question = questions[questions.find('QUESTION NO: '+str(testQ)):questions.find('QUESTION NO: '+str(testQ+1))]
			if (question.lower().find((wordMatch.lower()))!=-1):
				q = testQ
				break

if (randomQuestions=="0"):
	nextq = q+1
if (cgi.escape(os.environ["HTTP_USER_AGENT"])!="Mediapartners-Google"):
	os.system("echo "+str(q)+" >> /var/www/darts/tmp/webtest/"+testName+"/"+ident)
# dispQues
#question = questions[questions.find('QUESTION NO: '+str(q)):questions.find('QUESTION NO: '+str(q+1))]



print """
<form><p> <hr color=e6e6e6 size=3> <p> <input type=hidden name=id value="""+ident+"""><input type=hidden name=q value="""+str(nextq)+"""><input type=hidden name=r value="""+randomQuestions+"""><input type=hidden name=w 
value="""+wordMatch+"""><pre style=\"font-family:arial,courier,vernanda;\">"""+question.replace('A. ','<p><input type=checkbox name=a>A. ').replace('\nB. ','<br><input type=checkbox name=b>B. ').replace('\nC. ','<br><input type=checkbox name=c>C. ').replace('\nD. ','<br><input type=checkbox name=d>D. ').replace('\nE. ','<br><input type=checkbox name=e>E. ').replace('F. ','<br><input type=checkbox name=f>\nF. ').replace('\nG. ','<br><input type=checkbox name=g>G. ')+"""
</pre><p><input type=hidden name=n value="""+(str)((int)(number)+1)+"""><input type=submit><p>You have done """+number+""" questions.<br><a href=\"stop.py?id="""+ident+"""\">Check Score</a></form></div></body></html>
"""
#print "You got "+str(right)+" right."
#print "You got "+str(wrong)+" wrong."
#nothing = raw_input("Hit enter to exit.")
