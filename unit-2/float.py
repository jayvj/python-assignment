import re
num=raw_input("Enter float: ")
res=re.search('^[-+]?([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?$',num)
if res:
	print ("Valid float")
else:
	print ("Invalid float")

