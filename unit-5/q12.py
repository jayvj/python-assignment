def fldec2(fl):
	fli=float(fl)
	print ("\nFloating number:")
	print (fli)
	flo="{:+.2f}".format(fli)
	print ("\nFloating number upto 2 decimal places with a sign:")
	print (flo)
	fo.write(flo)


try:
	fi=open("fileq12ip.txt","r+")
	fo=open("fileq12op.txt","r+")
	fi.seek(0,0)
	fl=fi.read()
	fldec2(fl)	


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrint a floating number upto 2 decimal places with a sign is executed successfully!")


finally:
	print ("\nFinished.\n")
