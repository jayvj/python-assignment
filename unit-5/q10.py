def add_tags(tag,word):
	print ("\nHTML string with tags around the word(s):")
	print ("<%s>%s</%s>"%(tag,word,tag))
	

try:
	f=open("fileq1.txt","r+")
	f.seek(0,0)
	tag=raw_input("\nEnter tag: ")
	word=raw_input("\nEnter word(s): ")
	f.write("Tag:"+tag+'\n')
	f.write("Word(s):"+word)
	add_tags(tag,word)
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nCreating the HTML string with tags around the word(s) is executed successfully!")


finally:
	f.seek(0,0)
	f.truncate()
	print ("\nFinished.\n")
