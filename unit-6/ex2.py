import re
file=open("in_2.txt","r+")
line=file.read().split("\n")
#print(line)
def parse_start():
    try:
        file1=open("out_2.txt","w")
    except:
        print("Error Occured..!")
    for i in line:
        x=re.search(r"^<[a-z]+[0-9]*>$",i)
        y=re.search(r"^<[a-z]+[0-9]*>*",i)
        z=re.search(r"^</[a-z]+[0-9]*>$",i)
        w=re.search(r"<br>",i)
        if x:
            n=len(i)
            print("Start: ",i[1:n-1])
            file1.write("Start: "+i[1:n-1]+"\n")
        elif y:
            n=len(i)
            a=i[1:n].split(" ")
            print("Start: ",a[0])
            file1.write("Start: "+a[0]+"\n")
            result="{} data-model-target {} None".format("->",">")
            print(result)
            file1.write(result+"\n")
            result1="{} class {} 1".format("->",">")
            print(result1)
            file1.write(result1+"\n")
        elif z:
            n=len(i)
            print("End: ",i[2:n-1])
            file1.write("End: "+i[2:n-1]+"\n")
        elif w:
            n=len(i)
            print("Empty: ",i[1:n])
            file1.write("Empty: "+i[1:n]+"\n")
    file.close()
    file1.close()
parse_start()

