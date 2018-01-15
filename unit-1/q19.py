n=int(input("Enter the no of items in a dic:"))
dic={}
for d in range(n):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=raw_input("Enter value"+str(d+1)+": ")
	dic[key]=value
print ("Dictionary:")
print (dic)

key=raw_input("Enter key:")
if key in dic:
	print (key,"Given key already exists in a dictionary:")
else:
	print (key,"Given key does not exist in a dictionary:")
