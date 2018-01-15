from collections import Counter
def topthree(dic):
	d=Counter(dic)
	print (d)
	print ("Top three items in a shop:")
	for key,value in d.most_common(3):
		print ("%s %s" % (key,value))

n=int(input("Enter the no of items in a dic:"))
dic={}
for d in range(n):
	key=raw_input("Enter key"+str(d+1)+": ")
	value=raw_input("Enter value"+str(d+1)+": ")
	dic[key]=value
print ("Dictionary:")
print (dic)
topthree(dic)
