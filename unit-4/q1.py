def readlast():
	f.seek(0,0)
	lineno=int(input("Enter the no to read last n lines of a file: "))
	readline=n-lineno
	print ("\nReading last %d lines of a file"%lineno)
	for i in range(1,n+1):
		if i>readline:
			read=f.readline()
			print (read)
		else:
			f.readline()
	

try:
	n=int(input("\nEnter the no of lines in the file:"))
	f=open("file1.txt","r+")
	for i in range(n):
		text=raw_input("Enter string in line"+str(i+1)+" :")
		f.write(text+'\n')
	f.seek(0,0)
	line=f.read()
	print ("\nReading files:")
	print (line)
	readlast()
	f.seek(0,0)
	f.truncate()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nReading last n lines of a file is executed successfully!")


finally:
	print  ("\nFinished!\n")
