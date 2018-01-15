def setfn(set1,set2):
	print ("set1 is a superset of set2:")
	print (set1.issuperset(set2))
	print ("set2 is a subset of set1:")
	print (set1.issubset(set2))
	
n1=int(input("Enter the no of elements in set1:"))
set1=set()
print ("Set1:")
for i in range(n1):
	val=int(input("Enter val"+str(i+1)+": "))
	set1.add(val)
print ("Set1:")
print (set1)

n2=int(input("Enter the no of elements in set2:"))
set2=set()
print ("Set2:")
for i in range(n2):
	val=int(input("Enter val"+str(i+1)+": "))
	set2.add(val)
print ("Set2:")
print (set2)

setfn(set1,set2)
