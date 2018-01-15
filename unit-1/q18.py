n1=int(input("Enter the no of items in dic1:"))
dic1={}
for d in range(n1):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=raw_input("Enter value"+str(d+1)+": ")
	dic1[key]=value
print ("Dictionary:")
print (dic1)

n2=int(input("Enter the no of items in dic2:"))
dic2={}
for d in range(n2):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=raw_input("Enter value"+str(d+1)+": ")
	dic2[key]=value
print ("Dictionary:")
print (dic2)

concatdic={}
concatdic.update(dic1)
concatdic.update(dic2)
print ("Concatenate dictionaries:")
print (concatdic)
