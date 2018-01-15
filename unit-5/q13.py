def intpos(num,width):
	numi=int(num)
	val=numi/(10**(lnum-(width-1)))
	star='*'*(lnum-(width-1))
	res=str(val)+star
	print ("\nIntegers with '*':")
	print (res)
	fo.write(res)


try:
	fi=open("fileq13ip.txt","r+")
	fo=open("fileq13op.txt","r+")
	fi.seek(0,0)
	num=fi.read()
	lnum=len(num)-1
	print ("\nInteger: %s"%num)
	print ("\nLength of the integer: %d"%lnum)
	width=int(input("\nEnter the width to print * on the right of specified width: "))
	if width<=lnum:
		intpos(num,width)	
	else:
		print ("\nEnter the width less than or equal to length of int:%d!"%lnum)
		raise


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrint integers with '*' on the right of specified width is executed successfully!")


finally:
	print ("\nFinished.\n")
