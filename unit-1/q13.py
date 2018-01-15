lst1=[]
n=int(input("Enter the no of elements in list1:"))
for l in range(0,n):
	str1=raw_input("Enter val"+str(l+1)+": ")
	lst1.append(str1)
print (lst1)

lst2=[]
n=int(input("Enter the no of elements in list2:"))
for l in range(0,n):
	str1=raw_input("Enter val"+str(l+1)+": ")
	lst2.append(str1)
print (lst2)

lst1[-1:]=lst2
print ("After replacing the last element in a list with another list:")
print (lst1)
