import operator
n=int(input("Enter the no of items in a dic:"))
dic={}
for d in range(n):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=raw_input("Enter value"+str(d+1)+": ")
	dic[key]=value
print ("Dictionary:")
print (dic)

sortdic=sorted(dic.items(),key=operator.itemgetter(0))
print ("Dictionary in ascending by value:")
print (sortdic)
sortdic=sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
print ("Dictionary in descending by value:")
print (sortdic)

