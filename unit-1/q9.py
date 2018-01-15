lst=[]
n=int(input("Enter the no of elements in list:"))
for l in range(0,n):
	ele=int(input("Enter element"+str(l+1)+": "))
	lst.append(ele)
print (lst)

lst.sort()
print ("After sorting, the list is: ")
print (lst)
print ("Second largest number: ")
print (lst[n-2])
print ("Second smallest number: ")
print (lst[1])

