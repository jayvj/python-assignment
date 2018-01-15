def circiden():
	lst1=[]
	n1=int(input("Enter the no of elements in list1:"))
	for l in range(0,n1):
		ele=raw_input("Enter element"+str(l+1)+":")
		lst1.append(ele)
	print (lst1)
	lst2=[]
	n2=int(input("Enter the no of elements in list2:"))
	for l in range(0,n2):
		ele=raw_input("Enter element"+str(l+1)+":")
		lst2.append(ele)
	print (lst2)
	if n1!=n2:
		return False
	for x in range(0,n1):
		temp=lst1[0]
		lst1.remove(lst1[0])
		lst1.append(temp)
		if lst1==lst2:
			return True

val=circiden()
if(val):
	print ("Circularly identical")
else:
	print ("Not circularly identical")
