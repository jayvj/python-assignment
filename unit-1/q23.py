string=raw_input("Enter a string: ")
dic={}
for ch in string:
	dic[ch]=dic.get(ch,0)+1
print ("Dictionary from a string by tracking the count of the letters as values from the string:")
print (dic)
