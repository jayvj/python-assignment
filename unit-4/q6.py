def numsalage():
	numofrec=0
	f.seek(0,0)
	for line in f.readlines():
		numofrec+=1
	print ("Counting the number of records in that file: %d"%(numofrec-1))
	f.seek(0,0)
	next(f)
	print ("\nFor those who are getting salary less than Rs.4500 and aged more than 35:")
	print ("The employee numbers:")
	for line in f:
		list1=[]
		for word in line.split():
			list1.append(word)
		salary=int(list1[1])
		age=int(list1[2])
		if (salary<4500) and (age>35):
			print (list1[0])
				
				
try:
	f=open("file1.txt","r+")
	n=int(input("\nEnter the no of employees in the file:"))
	print ("\nEnter input:employeeno salary age in the file")
	f.write("employeeno salary age\n")
	f.seek(0,1)
	for i in range(n):
		text=raw_input("Enter string"+str(i+1)+" :")
		f.write(text+'\n')
	f.seek(0,0)
	text=f.read()
	print ("\nReading files:")
	print (text)
	numsalage()
	f.seek(0,0)
	f.truncate()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCounting the number of records in that file and also printing the employee numbers for those who are getting salary less than Rs.4500 and aged more than 35 are executed successfully!")


finally:
	print  ("\nFinished!\n")
