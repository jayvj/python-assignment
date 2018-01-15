def remdupindic(dic):
	uniquedic={}
	for key,value in dic.items():
		if value not in uniquedic.values():
			uniquedic[key]=value
	print ("Removing duplicates from Dictionary:")
	print (uniquedic)

n=int(input("Enter the no of items in a dic:"))
dic={}
for d in range(n):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=int(input("Enter value"+str(d+1)+": "))
	dic[key]=value
print ("Dictionary:")
print (dic)
remdupindic(dic)
