def sortbyval(dic):
	sortdic={}
	sortdic=sorted(dic.items(),key=lambda d:d[1],reverse=True)
	print ("Sort dictionary by value:")
	print (sortdic)
	
n=int(input("Enter the no of items in a dic:"))
dic={}
for d in range(n):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=int(input("Enter value"+str(d+1)+": "))
	dic[key]=value
sortbyval(dic)
