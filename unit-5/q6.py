def charchange(string):
	f.seek(0,0)
	list1=[]
	temp=[]
	for ch in string:
		list1.append(ch)
	temp=list1[1:]
	length=len(temp)	
	print ("\nChanging all occurrences of its first char changed to '$', except the first char itself from a given string:")
	ch=list1[0].lower()
	for i in range(length):
		letter=temp[i].lower()
		if letter==ch:
			list1[i+1]='$'
	print (list1)
		

try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter a string: ")
	f.write(string)
	charchange(string)
	f.seek(0,0)
	f.truncate()
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nGetting a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself is executed successfully!")

	
finally:
	print ("\nFinished.\n")
