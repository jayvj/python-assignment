n=int(input("Enter the no of tuples in a list:"))
lst=[]
tup=()
lval=int(input("Enter a number to replace last value of a tuples in a list:"))
for i in range(n):
	tup=tuple(map(int,raw_input("Enter tuple"+str(i+1)+": ").split(" ")))
	lst.append(tup)
	tup=()
print ("List:")
print (lst)
print ("Replace last value of tuples in a list:")
print ([t[:-1]+(lval,) for t in lst])
