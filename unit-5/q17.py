import re
import random
def passgen(pwd):
	if pwd=='w':
		weaklist=['b*+G2S','&3r)Xa','!U}w6X','\:wT7L','KP4t<(','dj4<Ek','W,/t5J',']4TQe{','dA[w5>]','z5<WkK']
		randweakpwd=random.choice(weaklist)
		print ("\nYour WEAK PASSWORD:")
		print (randweakpwd)
		fo.write("WEAK Password: "+randweakpwd)
	if pwd=='s':
		#randstrongpwd=strgen.StringGenerator(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~`!@#$%^&*_])')
		stronglist=[]
		for word in fi:
			w=word.split('\n')
			stronglist.append(w[0])
		randstrongpwd=random.choice(stronglist)
		print ("\nYour STRONG PASSWORD:")
		print (randstrongpwd)
		fo.write("STRONG Password: "+randstrongpwd)
	else:
		print ("\nWrong letter, you are pressed! Enter s for STRONG Password, w for WEAK Password.")
		raise
			

try:
	fi=open("fileq17ip.txt","r+")
	fo=open("fileq17op.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	pwd=raw_input("\nEnter s for STRONG Password or w for WEAK Password: ")
	passgen(pwd)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPassword generator in Python is executed successfully!")


finally:
	print ("\nFinished.\n")
