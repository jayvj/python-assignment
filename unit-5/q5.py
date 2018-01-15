def printstr(string,length):
	f.seek(0,0)
	list1=[]
	if length==2 or length==3:
		print ("\nResult: %s"%string)
		return 0
	if length==1:
		print ("\nResult: Empty string")
		return 0
	for ch in string:
		list1.append(ch)
	print (list1)	
	print ("\nGetting a string made of the first 2 and the last 2 chars from a given a string:")
	print (list1[0]+list1[1]+list1[length-2]+list1[length-1])
		

try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter a string: ")
	length=len(string)
	f.write(string)
	printstr(string,length)
	f.seek(0,0)
	f.truncate()
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nGetting a string made of the first 2 and the last 2 chars from a given a string, If the string length is less than 2, return instead of the empty string is executed successfully!")

	
finally:
	print ("\nFinished.\n")
