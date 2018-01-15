import re
emailid=raw_input("Enter an email_id: ")
res=re.search('^[a-zA-Z]+[\w\.]*@[a-zA-Z]+\.[a-zA-Z]+(\.[a-zA-Z]+)*$',emailid)
if res:
	print ("Valid emailid")
else:
	print ("Invalid emailid")
