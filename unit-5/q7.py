def ingly(string,length):
	f.seek(0,0)
	list1=[]
	keylist=['i','n','g']
	if length<3:
		print ("Result: %s"%string)
		return 0
	for ch in string:
		list1.append(ch)
	last=list1[-3:]
	if last==keylist:
		list1.extend(['l','y'])
	else:
		list1.extend(['i','n','g'])
	print ("\nAdding 'ing' or 'ly' at the end of a given string:")
	print ("".join(list1))


try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter a string: ")
	length=len(string)
	f.write(string)
	ingly(string,length)
	f.seek(0,0)
	f.truncate()
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPython program to add 'ing' at the end of a given string, If the given string already ends with 'ing' then add 'ly' instead and If the string length of the given string is less than 3, leave it unchanged is executed successfully!")

	
finally:
	print ("\nFinished.\n")
