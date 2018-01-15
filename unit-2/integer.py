import re
num=raw_input("Enter integer: ")
res=re.search('^[-,+]?[0-9]+[\L]?$',num)
if res:
	print ("Valid integer")
else:
	print ("Invalid integer")
