import urllib.request
import re
def email_no():
	try:
		f = urllib.request.urlopen('https://www.freecharge.in/app/contactus.htm')
		s = f.read().decode('utf-8')
		a=re.findall(r'[0-9]{2,4}[\-?][0-9]{8,10}',s)
		b=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
		print(a)
		print(b)
		f=open("out_8.txt","w")
		f.write(str(a))
		f.write("\n")
		f.write(str(b))
	except Exception as err:
 		print(err)
	finally:
		f.close()
email_no()

