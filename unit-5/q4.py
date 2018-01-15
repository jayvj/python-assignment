def remnpos(string,pos):
	f.seek(0,0)
	list1=[]
	for ch in string:
		list1.append(ch)
	i=0
	for word in list1:
			if i==pos:
				del list1[pos]
				break
			else:
				i+=1
	f.seek(0,0)
	f.truncate()
	for ch in list1:
		f.write(ch)
	
	
try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter a nonempty string: ")
	length=len(string)
	print ("\nLength of the string: %d"%length)
	f.write(string)
	pos=int(input("\nEnter the position to be removed from the string: "))
	if pos>length-1:
		print ("\nPosition exceeds the length of the string! Give position less than %d."%length)
		raise
	remnpos(string,pos)
	f.seek(0,0)
	text=f.read()
	print ("\nRemoving the %dth index character from a nonempty string %s:"%(pos,string))
	print (text)
	f.seek(0,0)
	f.truncate()
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nRemoving the nth index character from a nonempty string is executed successfully!")

	
finally:
	f.seek(0,0)
	f.truncate()
	print ("\nFinished.\n")
