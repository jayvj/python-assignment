def countword(sent):
	f.seek(0,0)
	dic={}
	for line in f:
		for word in line.split():
			if word not in dic.keys():
				dic[word]=1
			else:
				dic[word]=dic[word]+1
	print ("\nCounting the occurrences of each word in a given sentence:")
	print (dic)


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
	print ("\nCounting the occurrences of each word in a given sentence is executed successfully!")

	
finally:
	print ("\nFinished.\n")
