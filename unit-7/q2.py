class validparen:
	def is_valid_parentheses(self, str1):
        	stack= []
		pchar={"(": ")", "{": "}", "[": "]"}
        	for parenthesis in str1:
            		if parenthesis in pchar:
                		stack.append(parenthesis)
           	 	elif len(stack) == 0 or pchar[stack.pop()] != parenthesis:
                		return False
        	return len(stack) == 0


try:
	fo=open("opfileq2.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	end=''
	while end!='#':
		string=raw_input("\nEnter a string of parentheses ()/{}/[]: ")
		result=validparen().is_valid_parentheses(string)
		if result==0:
			print ("Invalid parentheses")
			fo.write("Invalid parentheses: "+string)
		else:
			print ("Valid parentheses")
			fo.write("Valid parentheses: "+string+"\n\n")
		end=raw_input("\nEnter # to stop this loop: ")


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nFinding the validity of a string of parentheses is executed successfully!")

	
finally:
	print ("\nFinished.\n")
