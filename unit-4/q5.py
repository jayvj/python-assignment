def copyupper(text):
	cf.write(text)
	cf.seek(0,0)
	print ("Copying one file to another:")
	copytext=cf.read()
	print (copytext)
	f.seek(0,0)
	cf.seek(0,0)
	for word in f.readlines():
		upword=word.upper()
		cf.write(upword)
	cf.seek(0,0)
	print ("Replacing all lower characters by their upper case equivalents:")
	replatext=cf.read()
	print (replatext)	
	

try:
	n=int(input("\nEnter the no of words in the file:"))
	f=open("file1.txt","r+")
	cf=open("copyfile1.txt","r+")
	for i in range(n):
		text=raw_input("Enter string"+str(i+1)+" :")
		f.write(text+'\n')
	f.seek(0,0)
	text=f.read()
	print ("\nReading files:")
	print (text)
	copyupper(text)
	f.seek(0,0)
	f.truncate()
	cf.seek(0,0)
	cf.truncate()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCopying one file to another and replacing all lower characters by their upper case equivalents are executed successfully!")


finally:
	print  ("\nFinished!\n")
