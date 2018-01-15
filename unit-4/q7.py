def mergesort(list1):
	for word in list1:
		mergef.write(word+str("\n"))
	mergef.seek(0,0)
	textmergef=mergef.read()
	print ("\nReading STUDENTS:")
	print (textmergef)


try:
	f1=open("file71.txt","r")
	f2=open("file72.txt","r")
	mergef=open("file7ms.txt","r+")
	textf1=f1.read()
	print ("\nReading LADIES:")
	print (textf1)
	textf2=f2.read()
	print ("\nReading GENTS:")
	print (textf2)
	f1.seek(0,0)
	list1=[]
	for line in f1:
		for word in line.split():
			list1.append(word)
	f2.seek(0,0)
	for line in f2:
		for word in line.split():
			list1.append(word)
	list1.sort()
	mergesort(list1)


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nProducing a third file STUDENTS which holds the merged list of the two given files in alphabetical order is executed successfully!")


finally:
	print  ("\nFinished!\n")
