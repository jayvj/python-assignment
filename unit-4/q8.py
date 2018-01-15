def studname():
	key=['F','T','T','T','T','T','F','T','F','T']
	lenkey=len(key)
	count=0
	f.seek(0,0)
	for line in f.readlines():
		count+=1
	f.seek(0,0)
	next(f)
	print ("Printing the names of the students who have secured more than 5 marks:")
	for line in f:
		list1=[]
		marks=0
		for word in line.split():
			list1.append(word)
		for i in range(1,lenkey+1):
			if list1[i]==key[i-1]:
				marks+=1
			else:
				marks-=0.5
		if marks>5:
			print (list1[0])


try:
	f=open("file8.txt","r+")
	text=f.read()
	print ("\nReading files:")
	print (text)
	studname()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrinting the names of the students who have secured more than 5 marks is executed successfully!")


finally:
	print  ("\nFinished!\n")
