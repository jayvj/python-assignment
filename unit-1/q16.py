def dicdepth(dic):
	if isinstance(dic,dict):
		return 1+(max(map(dicdepth,dic.values())) if dic else 0)
	return 0

dic={'a':1,'b':{'c':{'d':{'e':{}}}}}
print ("Dictionary:")
print (dic)
print ("Depth of a dictionary:")
print (dicdepth(dic))
