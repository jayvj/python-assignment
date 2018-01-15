import re
def romannumeral(string):
	res=re.search(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',string)
	if res:
		print ("\nValid Roman Numeral. True!")
		fo.write("Valid Roman Numeral: "+string)
	else:
		print ("\nInvalid Roman Numeral. False!")
		fo.write("Invalid Roman Numeral: "+string)


try:
	fo=open("fileq19op.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	string=raw_input("\nEnter string to validate whether it's a valid Roman numeral: ")
	romannumeral(string)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCreating a regular expression for a valid Roman numeral is executed successfully!")


finally:
	print ("\nFinished.\n")
