def unisort(comseq):
	for word in comseq:
		sepseq=word.split(',')
	uniseq=set(sepseq)
	list1=[]
	for word in uniseq:
		list1.append(word)
	list1.sort()
	print ("\nUnique words in sorted form:")
	print (list1)


try:
	f=open("fileq9.txt","r+")
	f.seek(0,0)
	string=f.read().split('\n')
	comseq=string[:-1]
	print ("\nPrint a comma separated sequence of words:")
	print (comseq)
	unisort(comseq)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nAccepting a comma separated sequence of words as input and printing the unique words in sorted form (alphanumerically) is executed successfully!")

	
finally:
	print ("\nFinished.\n")

