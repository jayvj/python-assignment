def swapstr(string,dot,comma):
	list1=[]
	for ch in string:
		list1.append(ch)
	i=0
	for ch in list1:
		if ch==dot:
			list1[i]=comma
			i+=1
		elif ch==comma:
			list1[i]=dot
			i+=1
		else:
			i+=1
	print ("\nSwapping comma and dot in a string:")
	res=''.join(list1)
	print (res)
	fo.write(res)


try:
	fi=open("fileq14ip.txt","r+")
	fo=open("fileq14op.txt","r+")
	fi.seek(0,0)
	st=fi.read().split('\n')
	list1=st[:-1]
	string=list1[0]
	print ("\nGiven string: %s"%string)
	dot='.'
	comma=','
	swapstr(string,dot,comma)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nSwapping comma and dot in a string is executed successfully!")


finally:
	print ("\nFinished.\n")
