import re
import random
def creditcard(ccnum):
	res=re.search(r'^[4-6]\d{3}\-\d{4}\-\d{4}\-\d{4}$',ccnum)	
	if res:
		print ("\nValid credit card number.")
		print (ccnum)
		fo.write("Valid credit card number: "+ccnum)
	else:
		print ("\nInvalid credit card number.")
		print (ccnum)	
		fo.write("Invalid credit card number: "+ccnum)	


try:
	fi=open("fileq21ip.txt","r+")
	fo=open("fileq21op.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	ccnolist=[]
	fi.seek(0,0)
	for num in fi:
		w=num.split('\n')
		ccnolist.append(w[0])
	ccnum=random.choice(ccnolist)	
	creditcard(ccnum)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nVerifing whether his credit card numbers are valid or not is executed successfully!")


finally:
	print ("\nFinished.\n")
