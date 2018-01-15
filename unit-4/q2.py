def longword(list1,maxlen):
	print ("The longest words in a file:")
	for word in list1:
		wordlength=len(word)
		if wordlength==maxlen:
			print (word)


try:
	n=int(input("\nEnter the no of words in the file:"))
	f=open("file1.txt","r+")
	list1=[]
	lenlist1=[]
	for i in range(n):
		text=raw_input("Enter string"+str(i+1)+" :")
		f.write(text+'\n')
		list1.append(text)
		lenlist1.append(len(text))
	maxlen=max(lenlist1)
	f.seek(0,0)
	text=f.read()
	print ("\nReading files:")
	print (text)
	longword(list1,maxlen)
	f.seek(0,0)
	f.truncate()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nFinding the longest words in a file is executed successfully!")


finally:
	print  ("\nFinished!\n")
