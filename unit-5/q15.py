def lastdeli(string,delimiter):
	res=string.rsplit(delimiter,1)
	print ("Splitting a string on the last occurrence of the delimiter:")
	print (res)
	for ch in res:
		fo.write(ch+'\t')


try:
	fi=open("fileq15ip.txt","r+")
	fo=open("fileq15op.txt","r+")
	fi.seek(0,0)
	st=fi.read().split('\n')
	list1=st[:-1]
	string=list1[0]
	print ("\nGiven string: %s"%string)
	delimiter=raw_input("\nEnter the delimiter for the string: ")
	flag=0
	for ch in string:
		if ch==delimiter:
			print ("\nDelimiter is present in the given string!")
			flag=1
			break
		else:
			continue
	if flag==0:
		print ("\nEnter the valid delimiter present in the given string!")
		raise
	lastdeli(string,delimiter)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nSplitting a string on the last occurrence of the delimiter is executed successfully!")


finally:
	print ("\nFinished.\n")
