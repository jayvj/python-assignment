list1=[]
n=int(input("Enter the no of elements in a list:"))
for l in range(0,n):
	val=int(input("Enter val"+str(l+1)+":"))
	list1.append(val)

list2=set()
finlist=[]
for l in list1:
	if l not in list2:
		finlist.append(l)
		list2.add(l)

print("After removing duplicates from a list:")
print(finlist)
