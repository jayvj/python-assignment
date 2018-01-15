lst1=[]
n1=int(input("Enter the no of color_name in list1:"))
for l in range(0,n1):
	str1=raw_input("Enter val"+str(l+1)+": ")
	lst1.append(str1)
print (lst1)

lst2=[]
n2=int(input("Enter the no of color_code in list2:"))
for l in range(0,n2):
	str1=raw_input("Enter val"+str(l+1)+": ")
	lst2.append(str1)
print (lst2)

if n1!=n2:
	print ("Dictionary cannot be formed!")

dictionary={}
lst3=[]
for i in range(0,n2):
	dictionary={'color_name':lst1[i],'color_code':lst2[i]}
	lst3.append(dictionary)
print ("Convert list to list of dictionaries:")
print (lst3)
