class getupper:
	def __init__(self):
		self.string=""
	def get_String(self):
		self.string=raw_input("\nEnter string: ")
		fo.write("Given string: "+self.string)
	def print_String(self):
		upper=self.string.upper()
		print ("\nString in upper case:")
		print (upper)
		fo.write("\nString in upper case: "+upper)
	
	
try:
	fo=open("opfileq7.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	str1=getupper()
	str1.get_String()
	str1.print_String()
		

except IOError:
	print ("\nAn error occured trying to read the file.")
#except:
	#print ("\nAn error occured.")


else:
	print ("\nget_String accept a string from the user and print_String print the string in upper case is executed successfully!")

	
finally:
	print ("\nFinished.\n")
