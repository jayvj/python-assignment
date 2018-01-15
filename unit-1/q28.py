n=int(input("Enter the no of tuples in a list:"))
lst=[]
tup=()
for i in range(n):
	tup=tuple(raw_input("Enter a string and a float element in tuple"+str(i+1)+": ").split(" "))
	lst.append(tup)
	tup=()
print ("List:")
print (lst)
sortlst=[]
sortlst=sorted(lst,key=lambda fl:float(fl[1]),reverse=True)
print ("Sort a tuple by its float element:")
print (sortlst)
