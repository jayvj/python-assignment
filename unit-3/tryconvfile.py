def listconvertion(list1):
	print ("Reading file in list format:")
	print (list1)
	print ("Converting list into set:")
	set1=set(list1)
	print (set1)
	print ("Converting list into tuple:")
	tuple1=tuple(list1)
	print (tuple1)
	print ("Converting list into dictionary:")
	dict1={}
	for key in list1:
		if dict1.has_key(key):
			dict1[key]=dict1[key]+1
		else:
			dict1[key]=1
	print (dict1)


def setconvertion(set1):
	print ("Reading file in set format:")
	print (set1)
	print ("Converting set into list:")
	list1=list(set1)
	print (list1)
	print ("Converting set into tuple:")
	tuple1=tuple(set1)
	print (tuple1)
	print ("Converting set into dictionary:")
	dict1={}
	for key in set1:
		if dict1.has_key(key):
			dict1[key]=dict1[key]+1
		else:
			dict1[key]=1
	print (dict1)


def tupleconvertion(tuple1):
	print ("Reading file in tuple format:")
	print (tuple1)
	print ("Converting tuple into list:")
	list1=list(tuple1)
	print (list1)
	print ("Converting tuple into set:")
	set1=set(tuple1)
	print (set1)
	print ("Converting tuple into dictionary:")
	dict1={}
	for key in tuple1:
		if dict1.has_key(key):
			dict1[key]=dict1[key]+1
		else:
			dict1[key]=1
	print (dict1)


def dictconvertion(dict1):
	print ("Reading file in dictionary format:")
	print (dict1)
	print ("Converting dictionary into list:")
	list1=list(dict1)
	print (list1)
	print ("Converting dictionary into set:")
	set1=set(dict1)
	print (set1)
	print ("Converting dictionary into tuple:")
	tuple1=tuple(dict1)
	print (tuple1)


try:
	n=int(input("\n\nEnter the no of int: "))
	f=open("file.txt","w+")
	list1=[]
	set1=set()
	tuple1=()
	dict1={}
	for i in range(n):
		num=raw_input("Enter integer"+str(i+1)+": ")
		f.write(num+' ')
		list1.append(num) 
		set1.add(num)
		if dict1.has_key(num):
			dict1[num]=dict1[num]+1
		else:
			dict1[num]=1
	print ("\n\nList Convertion:")
	listconvertion(list1)
	print ("\n\nSet Convertion:")
	setconvertion(set1)
	print ("\n\nTuple Convertion:")
	tuple1=tuple(list1)
	tupleconvertion(tuple1)
	print ("\n\nDictionary Convertion:")
	dictconvertion(dict1)


except IOError:
	print ("\n\nAn error occured trying to read the file.")
except ValueError:
	print ("\n\nNon-numeric data found in the file.")
except ImportError:
	print ("\n\nNO module found.")
except EOFError:
	print ("\n\nEnd of file.")
except KeyboardInterrupt:
	print ("\n\nYou cancelled the operation.")
except:
	print ("\n\nAn error occured.")


else:
	print ("\n\nInterconversions of list, set, tuple and dictionary using files are executed successfully!")


finally:
	print  ("\n\nFinished!\n\n")
