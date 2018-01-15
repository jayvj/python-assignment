class subsets:  
    def sub1(self, s1):  
        return self.sub2([], sorted(s1))  
 
    def sub2(self, curr, s1):  
        if s1:  
            return self.sub2(curr, s1[1:]) + self.sub2(curr + [s1[0]], s1[1:])  
        return [curr]  


try:
	fo=open("opfileq3.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	n=int(input("\nEnter the number of elements: "))
	list1=[]
	fo.write("All possible unique subsets from a set of distinct integers: ")
	for i in range(n):
		num=int(input("Enter num"+str(i+1)+": "))
		fo.write(str(num))
		list1.append(num)
	print ("\nSet of distinct integers:")
	print (list1)
	print ("\nAll possible unique subsets from a set of distinct integers:") 
	res=subsets().sub1(list1)
	print (res)
	fo.write("\n"+str(res))


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nGetting all possible unique subsets from a set of distinct integers is executed successfully!")

	
finally:
	print ("\nFinished.\n")
