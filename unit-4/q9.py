def wordvoca():
	fvoc.seek(0,0)
	for line in fvoc:
		for word in line.split():
			ch=word[:1].lower()
			if ch=='s':
				fwords.write(word+str("\n"))
	fwords.seek(0,0)	
	words=fwords.read()
	print ("Reading WORDS:")
	print (words)
	

try:
	fvoc=open("file9.txt","r+")
	fwords=open("file9word.txt","r+")
	text=fvoc.read()
	print ("\nReading VOCABULARY:")
	print (text)
	wordvoca()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nWriting in another file WORDS, the words beginning with the character S or s from the 1000 words is executed successfully!")


finally:
	print  ("\nFinished!\n")
