lst=[]
n=int(input("Enter the no of elements in a list:"))
for l in range(0,n):
	val=int(input("Enter val"+str(l+1)+":"))
	lst.append(val)
print (lst)

remeven=[]
for x in lst:
	if x%2 != 0:
		remeven.append(x)
print ("After removing even numbers from a list:")
print (remeven)
		
