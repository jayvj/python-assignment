from collections import Counter

n1=int(input("Enter the no of items in a dic1:"))
n2=int(input("Enter the no of items in a dic2:"))

dic1,dic2={},{}
print("Dictionary1:")
for d in range(n1):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=int(input("Enter value"+str(d+1)+": "))
	dic1[key]=value
print ("Dictionary1:")
print (dic1)

print("Dictionary2:")
for d in range(n2):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=int(input("Enter value"+str(d+1)+": "))
	dic2[key]=value
print ("Dictionary2:")
print (dic2)

combinedic=Counter(dic1) + Counter(dic2)
print ("Combine two dictionary adding values for common keys:")
print (combinedic)
