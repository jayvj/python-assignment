lst=[]
n=int(input("Enter the no of elements in a list:"))
for l in range(0,n):
	ele=raw_input("Enter element"+str(l+1)+": ")
	lst.append(ele)
print (lst)
length=len(lst)
range1=int(input("Enter the range goes from 1 to n: "))

concatlst=[]
for r in range(1,range1+1):
	for i in range(0,length):
		element=lst[i]+str(r)
		concatlst.append(element)
print ("Concatenating a given list which range goes from 1 to n:")
print (concatlst)
