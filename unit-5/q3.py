def countword(sent):
	f.seek(0,0)
	set1=set()
	for line in f:
		for word in line.split():
			print word
			set1.add(word)
	print ("\nList of words:")
	print (set1)
	max1=max(set1)
	print ("\nLength of the longest one:")
	print (max1)
	

try:
	f=open("fileq1.txt","r+")
	sent=raw_input("\nEnter a sentence: ")
	f.write(sent)
	countword(sent)
	f.seek(0,0)
	f.truncate()
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPython function that takes a list of words and returns the length of the longest one is executed successfully!")

	
finally:
	print ("\nFinished.\n")
