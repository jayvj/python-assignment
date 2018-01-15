list1=[]
n1=int(input("Enter the no of elements in list1:"))
for l in range(0,n1):
	val=int(input("Enter val"+str(l+1)+":"))
	list1.append(val)
print (list1)

list2=[]
n2=int(input("Enter the no of elements in list2:"))
for l in range(0,n2):
	val=int(input("Enter val"+str(l+1)+":"))
	list2.append(val)
print (list2)

list1[:0]=list2
print ("Extend a list without append:")
print (list1)

