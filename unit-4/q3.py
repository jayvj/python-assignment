def freqword():
	words=file("file1.txt","r+").read().split()
	uniqWords = sorted(set(words))
	for word in uniqWords:
    		print ("Count of the word %s: %d"%(word,words.count(word)))
		

try:
	n=int(input("\nEnter the no of words in the file:"))
	f=open("file1.txt","r+")
	for i in range(n):
		text=raw_input("Enter string"+str(i+1)+" :")
		f.write(text+'\n')
	f.seek(0,0)
	text=f.read()
	print ("\nReading files:")
	print (text)
	freqword()
	f.seek(0,0)
	f.truncate()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCounting the frequency of words in a file is executed successfully!")


finally:
	print  ("\nFinished!\n")
