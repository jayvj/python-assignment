def formatdic(format1,length):
	forlist=[]
	for word in format1:
		w=word.split('\n')
		lenwor=len(w)
		if lenwor==1:
			forlist.append(w[0])
		else:
			forlist.append(w[0])
			forlist.append(w[1])
	del forlist[-1]
	return (forlist)
def dic(formats):
	dict1={}
	for word in formats:
		if word not in dict1.keys():
			dict1[word]=1
		else:
			print ("Same format cannot appear again in the combination:")
			return False
	return True
			
			
def textformat():
	f.seek(0,0)
	print ("\nFormatting for the given text:")
	for line in f:
		str1=[]
		format1=[]
		for word in line.split(" with format "):
			str1.append(word)
		strings=str1[0]
		formats=str1[1]
		for word in formats.split(" and "):
			format1.append(word)
		length=len(format1)
		formats=formatdic(format1,length)
		if dic(formats):
			print ("\n")
		else:
			print ("Duplication is not allowed:")
			return 0
		if length==1:
			print ("<%s>%s</%s>"%(formats[0],strings,formats[0]))
		if length==2:
			print ("<%s><%s>%s</%s></%s>"%(formats[0],formats[1],strings,formats[0],formats[1]))
		if length==3:
			print ("<%s><%s><%s>%s</%s></%s></%s>"%(formats[0],formats[1],formats[2],strings,formats[0],formats[1],formats[2]))
		if length==4:
			print ("<%s><%s><%s><%s>%s</%s></%s></%s></%s>"%(formats[0],formats[1],formats[2],formats[3],strings,formats[0],formats[1],formats[2],formats[3]))
		

try:
	f=open("file10.txt","r+")
	text=f.read()	
	print ("\nReading files:")
	print (text)
	textformat()	


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nWriting text into a file that specifies formatting for the given text is executed successfully!")


finally:
	print  ("\nFinished!\n")
