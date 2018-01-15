import re
def notpoor(string):
	f.seek(0,0)
	text=re.sub(r'(not.*?(poor|bad))',"good",string,count=1)
	print ("\nAfter replacing with good:")
	print (text)

try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter a sentence ...not...poor/bad...: ")
	f.write(string)
	notpoor(string)
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nFinding the first appearance of the substring 'not' and 'poor/bad' from a given string and replacing with good is executed successfully!")

	
finally:
	f.seek(0,0)
	f.truncate()
	print ("\nFinished.\n")

