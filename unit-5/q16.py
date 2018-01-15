import random
def hangman(list1,ranword,length):
	print ("\nRULES for this game:")
	print ("Don't enter the same letter.")
	print ("You can get a hint at your 4th wrong letter.")
	print ("You will be lose at your 6th wrong letter.")
	limit=6
	tries=4
	count=0
	add=0
	flag=0
	countflag=0
	hintflag=0
	print ("\nNo of letters for your word is %d."%length) 
	print ("Initially your word:") 
	list2=['']*length
	listletter=[]
	print (list2)
	print ("You have only 6 counts to lose your game!")
	inc=1
	print ("\nGAME START! After entering your letter, press Enter key:")
	while count<6:
		letcount=0
		letter=raw_input("\nTry"+str(inc)+": ")
		if letter not in listletter:
			listletter.append(letter)
		else:
			print ("The letter is already given. Give alternate letter.")
			continue
		inc+=1
		for i in range(length):
			if letter not in list1:
				print ("Wrong letter! Go for next try!")
				count+=1
				countflag=1
				break
			elif letter==list1[i]:
				letcount=list1.count(letter)
				pos=i
				countflag=0
				list2[pos]=letter
		if countflag!=0:
			print ("%d counts more!"%(limit-count))
		elif countflag==0:
			add+=letcount
		print ("Your word:")
		print (list2)
		if add==length:
			print ("\nGame is successfully completed!")
			print ("The word is %s"%ranword)
			flag=1
			break;
		if count>=tries and hintflag==0:
			hint=raw_input("\nIf you want HINT for the word,press s: ")
			if hint=='s':
				print ("HINT for this word:")
				print (dic[ranword])
				hintflag=1
			else:
				print ("Your HINT is neglected. Continue your game!")
	if flag==0:
		print ("\nGAME OVER! YOU LOST IN THIS GAME!")
		print ("The word is %s"%ranword)
			
try:
	fi=open("fileq16ip.txt","r+")
	fi.seek(0,0)
	dic={}
	for line in fi:
		(word,hint)=line.split()
		dic[word]=hint
	ranword=random.choice(dic.keys())
	list1=[]
	for ch in ranword:
		list1.append(ch)
	length=len(ranword)
	hangman(list1,ranword,length)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nThe game of Hangman is executed successfully!")


finally:
	print ("\nFinished.\n")
