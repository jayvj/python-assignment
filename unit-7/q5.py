import simplejson
class zerosum:
	def threesum(self,arr,n):
		found = True
		print ("\nThe three elements that sum to zero from the given array:")
		simplejson.dump(arr,fo)
		fo.write("\nThe three elements that sum to zero from the given array:\n")
		for i in range(0, n-2):
			for j in range(i+1, n-1):
				for k in range(j+1, n):
					if arr[i] + arr[j] + arr[k] == 0:
						print(arr[i], arr[j], arr[k])
						fo.write("("+str(arr[i])+","+str(arr[j])+","+str(arr[k])+")\n")
						found = True
		if found == False:
			print("Three elements that sum to zero does not exist in the given array!")


try:
	fi=open("ipfileq5.txt","r+")
	fo=open("opfileq5.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	fi.seek(0,0)
	list1=[]
	for val in fi:
		ele=val.strip("\n")
		num=int(ele)
		list1.append(num)
	print ("\nThe given array:")
	print (list1)
	length=len(list1)
	obj=zerosum()
	obj.threesum(list1,length)
	
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nFinding the three elements that sum to zero from a set of n real numbers is executed successfully!")

	
finally:
	print ("\nFinished.\n")
