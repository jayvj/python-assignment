list1=[]
sumlist=[]
pos=0

n=int(input("Enter the no of elements in a list:"))
lno=int(input("Enter the no of sublists in a list:"))
for l in range(0,lno):
	print ("Enter sublist"+str(l+1)+": ")
	lst=[]
	sum1=0
	for i in range(0,n):
		val=int(input("Enter element"+str(i+1)+": "))
		sum1+=val
		lst.append(val)
	list1.append(lst)
	sumlist.append(sum1)
	if sumlist[pos]<sumlist[l]:
		pos=l
print (list1)

print ("Sumlist:")
print (sumlist)
print ("Maximum sum:")
print (max(sumlist))
print ("The highest sum sublist:")
print (list1[pos])
