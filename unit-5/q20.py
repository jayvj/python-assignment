import re
import random
def empuid(uidnum):
	res=re.search(r'([A-Z]{2}\d{3}[a-z]*|\d{3,}[A-Z]{2,}[a-z]*|[a-z]*[A-Z]{2,}\d{3,}|[a-z]*\d{3,}[A-Z]{2,}|[A-Z]{2,}[a-z]*\d{3,}|\d{3,}[a-z]*[A-Z]{2,})',uidnum)	
	if res:
		print ("\nValid UID.")
		print (uidnum)
		fo.write("Valid UID: "+uidnum)
	else:
		print ("\nInvalid UID.")
		print (uidnum)	
		fo.write("Invalid UID: "+uidnum)
		raise	


try:
	fi=open("fileq20ip.txt","r+")
	fo=open("fileq20op.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	uidlist=[]
	fi.seek(0,0)
	for num in fi:
		w=num.split('\n')
		uidlist.append(w[0])
	uidnum=random.choice(uidlist)	
	empuid(uidnum)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCreating a unique identification number (UID) for each of its employees is executed successfully!")


finally:
	print ("\nFinished.\n")
