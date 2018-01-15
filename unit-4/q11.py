import csv
def arrayunion():
	csvlist=[]
	f.seek(0,0)
	next(f)
	for line in csv.reader(f,delimiter='#'):
		csvlist.append(line)
	print ("\nPrint each row in the file in array format:")
	for row in csvlist:
		print (row)
	print ("\nPrint the array of union:")
	print (csvlist)
	namelist=[]
	for item in csvlist:
		namelist.append(item[0])
	print ("\nPrint the names before sorting:")
	print (namelist)
	print ("\nPrint the names in alphabetic order:")
	namelist.sort()
	print (namelist)
			
try:
	f=open("file11.csv","r+")
	text=f.read()
	print ("\nReading files:")
	print (text)
	arrayunion()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCreating an array of union and Printing the names in alphabetic order is executed successfully!")


finally:
	print  ("\nFinished!\n")
