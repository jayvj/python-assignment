import collections
lst=[]
n=int(input("Enter the no of elements in a list:"))
for l in range(0,n):
	ele=int(input("Enter element"+str(l+1)+": "))
	lst.append(ele)
print (lst)

count=collections.Counter(lst)
print ("Frequency of the elements in a list: ")
print (count)
