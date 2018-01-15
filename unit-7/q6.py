class revstr:
	def rev(self,string):
		word=string.split(" ")
		word=word[-1::-1]
		reverse=' '.join(word)
		return reverse


try:
	fo=open("opfileq6.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	string=raw_input("\nEnter string: ")	
	fo.write("The given string: ")
	fo.write(string)
	revword=revstr().rev(string)
	print ("\nReversing a string word by word:")
	fo.write("\n\nReversing a string word by word: ")
	print (revword)
	fo.write(revword)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nReversing a string word by word is executed successfully!")

	
finally:
	print ("\nFinished.\n")
