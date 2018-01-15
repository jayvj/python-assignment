import itertools
def combineletters(dic):
	print ("All combinations of letters, selecting each letter from a different key in a dictionary:")
	for comblet in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
		str1=''.join(comblet)
		print (str1)

n=int(input("Enter the no of items in a dic:"))
dic={}
for d in range(n):
	key=raw_input("Enter key"+str(d+1)+": ")
	valno=int(input("Enter the no of values for this key in dic: "))
	for v in range(valno):
		value=raw_input("Enter value"+str(d+1)+": ")
		dic.setdefault(key,[]).append(value)
print ("Dictionary:")
print (dic)
combineletters(dic)
