import csv
def empsalary():
	period=30
	print ("Let us consider the salary for the period 30 days in a month for employees: %d"%period)
	csvlist=[]
	f.seek(0,0)
	next(f)
	for line in csv.reader(f,delimiter='#'):
		csvlist.append(line)
	print ("\nPrint each row in the file in array format:")
	for row in csvlist:
		print (row)
	dic={}
	for item in csvlist:
		sal=int(item[1])
		leave=int(item[2])
		namesal=[]
		da=(120/100)*sal
		salary=sal+da
		if leave>10:
			extradays=leave-10
			totdays=period-extradays
			orisalary=(totdays*salary)/period
			namesal.append(item[0])
			namesal.append(orisalary)
			dic[item[0]]=orisalary
		else:
			namesal.append(item[0])
			namesal.append(salary)
			dic[item[0]]=salary
	print ("\nempname: salary:")
	for key in sorted(dic):
		print ("%s: %d"%(key,dic[key]))


try:
	f=open("q12firstexcelpython.csv","r+")
	text=f.read()
	print ("\nReading files:")
	print (text)
	empsalary()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nComputing the monthly pay of 100 employees and Printing the name and the salary list sorted by name is executed successfully!")


finally:
	print  ("\nFinished!\n")
