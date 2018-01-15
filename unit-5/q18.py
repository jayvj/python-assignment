import re
def pwdvalid(pwd):
	flag=0
	strong=re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~`!@#$%^&*_]).{11,20}',pwd,re.M)
	if strong:
		print ("\nStrong Password!")
		fo.write("Strong Password: "+pwd)
		return 0
	weak=re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~`!@#$%^&*_]).{5,10}',pwd,re.M)
	if weak:
		print ("\nWeak Password!")
		fo.write("Weak Password: "+pwd)
		return 0
	if flag==0:
		print ("\nInvalid Password!")
		fo.write("Invalid Password: "+pwd)


try:
	fo=open("fileq18op.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	pwd=raw_input("\nEnter a password: ")
	pwdvalid(pwd)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPassword strength validator in Python is executed successfully!")


finally:
	print ("\nFinished.\n")
