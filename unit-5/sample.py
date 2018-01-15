#import re
#emailid=raw_input("Enter password: ")
#res=re.search(r'[A-Z]+[a-z]+\d+.+',emailid,re.M)
#res=re.search(r'[A-Z]+[a-z]+\d+.+(\w*.*|.*\w*)',emailid,re.M)
#res=re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~`!@#$%^&*_])',emailid,re.M)
#res=re.search(r'(.*\d)(.*[a-z])(.*[A-Z])(.*[~`!@#$%^&*_])',emailid,re.M)
#res=re.search(r'(?=\d)(?=[a-z])(?=[A-Z])(?=[~`!@#$%^&*_])',emailid,re.M)
#if res:
#	print ("Valid emailid")
#else:
#	print ("Invalid emailid")

import re
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
#if re.search(pattern, 'XCCMCI'):
if re.search(pattern, 'MCMXCVIII'):
    print 'Valid Roman'
else:
    print 'Not valid Roman'
	#res=re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~`!@#$%^&*_]).{11,20}',pwd,re.M)
	#res=re.search(r'(((?=[a-z]*\d{3,})(?=[a-z]*[A-Z]{2,})).{10}){1}',uidnum,re.M)
	#res=re.search(r'(((?=[A-Z]{2,})(?=\d{3,})[a-zA-Z0-9]*).{1,10}){1}',uidnum,re.M)	
	#res=re.search(r'[A-Z]{2,}[0-9]{3,}[a-zA-Z0-9]*|[0-9]{3,}[A-Z]{2,}[a-zA-Z0-9]*',uidnum,re.M)
	#res=re.search(r'([A-Z]{2,})([0-9]{3,})([a-z]*)',uidnum,re.M)	
	#res=re.search(r"^((?:[A-Z]{2})(?:[0-9]{3})([a-z]{5}))$",uidnum)		

