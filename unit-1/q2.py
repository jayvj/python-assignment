def match(strings):
	count=0
	for str in strings:
		if len(str)>=2 and str[0]==str[-1]:
			count+=1
	return count

lst=[]
n=int(input("Enter the no of elements in a list:"))
for l in range(0,n):
	ele=raw_input("Enter element"+str(l+1)+":")
	lst.append(ele)
print (lst)

n=match(lst)
print ("Count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings:")
print (n)
