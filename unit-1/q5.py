lst=[]
n=int(input("Enter the no of characters in a list:"))
for l in range(0,n):
	ch=raw_input("Enter character"+str(l+1)+":")
	lst.append(ch)
print (lst)

string=''.join(lst)
print ("List of characters into a string:")
print (string)
