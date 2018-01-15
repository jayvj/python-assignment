n1=int(input("Enter the no of items in a dic1:"))
dic1={}
for d in range(n1):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=int(input("Enter value"+str(d+1)+": "))
	dic1[key]=value
print ("Dictionary1:")
print (dic1)

n2=int(input("Enter the no of items in a dic2:"))
dic2={}
for d in range(n2):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=int(input("Enter value"+str(d+1)+": "))
	dic2[key]=value
print ("Dictionary2:")
print (dic2)

flag=0
for key in dic1:
	if key in dic2:
		if dic1[key]==dic2[key]:
			value=dic1.get(key)
			print ("%s: %d is present in both dic1 and dic2"%(key,value))
			flag=1
if flag==0:
	print ("No match in key values in two dictionaries!")
