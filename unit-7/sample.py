import re
fi=open("ipfileq1.txt","r+")
fi.seek(0,0)
for val in fi.readlines():
	ele=val.strip("\n")
	print (ele)
	num=re.search(r'\d+',val,re.M)
	if num:
		print ("yes")
	else:
		print ("NO")

def is_valid_parentheses(self, str1):
        stack= []
	pchar={"(": ")", "{": "}", "[": "]"}
        for parenthesis in str1:
            if parenthesis in pchar:
                stack.append(parenthesis)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthesis:
                return False
        return len(stack) == 0


def findTriplets(arr, n):
 
    found = True
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
             
    # If no triplet with 0 sum 
    # found in array
    if (found == False):
        print(" not exist ")
