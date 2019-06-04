import datetime

print ('"Waiting in the lobby...alone"\n"Some approaches"') 
strinput = str(input())  
while(strinput.lower() != "hello"):	
	print ('Pepper - i am the robot here, yet i know you need to start a conversation with "hello"')
	strinput = str(input()) 
else:
	print('Pepper - Hi i am Pepper, do you have an appointment?')

strinput = str(input())
while(strinput.lower() != "yes" and strinput.lower() != "no"):	
	print ('Pepper - Just "yes" or "no" would be fine')
	strinput = str(input())
if(strinput.lower() == "no"):
	print ('Pepper - well then, please contact xxx-xxxx-xxxx if u want to make one\nPepper - Have a good day')
else:
	f = open("appointments.txt", "r")
	mylist = list(f)
	flag=False
	while(flag == False):
		print ('Pepper - can i have your name please, so that i could check for the appointment		\nPepper - please note that i need both first and last name to proceed ')
		strinput = str(input())
		strname=strinput.split()
		while(len(strname) != 2):
			print ('Pepper - please note that i need both first and last name to proceed with the check\nPepper - Please try again ')
			strinput = str(input())
			strname=strinput.split()
		strchecker='visitorName '
		strchecker += strname[0]
		strchecker += ' '
		strchecker += strname[1]

		strchecker2='visitorName '
		strchecker2 += strname[1]
		strchecker2 += ' '
		strchecker2 += strname[0]

		i=0
		for x in mylist:
			i=i+1
			if((str(x.rstrip()).lower() == strchecker.lower()) or (str(x.rstrip()).lower() == strchecker2.lower())):
				flag=True
				break
		if (flag == False):
			print('Pepper - It seems that the name you have given does not exist, please try again :')


	stremploy=mylist[i].replace('employeeName','')

	print('Pepper - Can you confirm that you have an appointment with' + stremploy.rstrip() + '?' )
	strinput = str(input())
	while(strinput.lower() != "yes" and strinput.lower() != "no"):	
		print('Pepper - Can you confirm that you have an appointment with' + stremploy.rstrip() + '?' )
		print ('Pepper - a "yes" or "no" answer would be fine')
		strinput = str(input())
	if(strinput.lower() == "no"):
		print ('Pepper - There seems to be a problem with the appointments since you have been listed with another host.\nPlease contact "xxx-xxxx-xxxx" and try again')
	else:
		checkins_append = open("checkins.txt", 'a+')
		checkins_read = open("checkins.txt", 'r')
		checklist= list(checkins_read)
		now = datetime.datetime.now()
		strcheckin = str(mylist[i-2]).rstrip().replace('appointmentId ','')+ ' ' + str(now) + '\n'
		for x in checklist:
			if(x[0] == strcheckin[0]):
				print ('Pepper - You have already checked in')
				flag = False
		if(flag==True):
			checkins_append.write(strcheckin)
			print ('Pepper - You have been checked-in, please wait in the reception for your host')	
		checkins_append.close()
		checkins_read.close()

	
