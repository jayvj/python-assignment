def cipher(lowch,pos):
	list1=[]
	for ch in lowch:
		if ch>='a' and ch<='z':
			c=ord(ch)-97
			enc=chr((c+pos)%26+97)
			list1.append(enc)
		elif ch==' ':
			list1.append('#')
			continue
		else:
			list1.append(ch)
			continue
	print ("\nCreating a Caesar encryption:")
	print (''.join(list1))	


try:
	f=open("fileq1.txt","r+")
	string=raw_input("\nEnter a plaintext: ")
	f.write(string)
	pos=int(input("\nEnter the position to replace a letter down the alphabet: "))
	lowch=string.lower()
	cipher(lowch,pos)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCreating a Caesar encryption in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet is executed successfully!")


finally:
	f.seek(0,0)
	f.truncate()
	print ("\nFinished.\n")
