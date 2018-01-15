import simplejson
class pairind:
   def targetsum(self, nums, target):
        for i,val in enumerate(nums):
		if val < target:
			pair=target - val
			if pair in nums:
				i2=nums.index(pair)
				print ("Index%d and Index%d"%(i,i2))
				return i,i2
				break


try:
	fo=open("opfileq4.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	n=int(input("\nEnter the number of elements: "))
	list1=[]
	fo.write("The given array: ")
	for i in range(n):
		num=int(input("Enter num"+str(i+1)+": "))
		list1.append(num)
	simplejson.dump(list1,fo)
	print ("\nThe given array:")
	print (list1)
	target=int(input("\nEnter target number for sum: "))
	print ("\nIndices of two nos from array whose sum equals a specific target number:") 
	ind1,ind2=pairind().targetsum(list1,target)
	fo.write("\nIndices of two nos from array whose sum equals a specific target number:")
	fo.write("\n"+"Index"+str(ind1)+" and "+"Index"+str(ind2))


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nFinding a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number is executed successfully!")

	
finally:
	print ("\nFinished.\n")
