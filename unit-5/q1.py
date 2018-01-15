def countfreq(string):
	f.seek(0,0)
	dic={}
	for ch in string:
		if ch not in dic.keys():
			dic[ch]=1
		else:
			dic[ch]=dic[ch]+1
	print ("\nCounting the number of characters (character frequency) in a string:")
	print dic
	

try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter string: ")
	f.write(string)
	countfreq(string)
	f.seek(0,0)
	f.truncate()
	
	
except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")

	
else:
	print ("\nCounting the number of characters (character frequency) in a string is executed successfully!")

	
finally:
	print ("\nFinished.\n")
