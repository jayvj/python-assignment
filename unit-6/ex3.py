import re
file=open("in_3.txt","r+")
line=file.readlines()
def data():
    s=line[3].split(" ")
    if re.match(r"^<[a-z]+>$",s[0]):
        print("data:\n",s[1])
data()
def single_multi():
    string=""
    for i in line[0:3]:
        x=re.search(r"^<!--.*-->",i)
        y=re.search(r"^<!--.*|\n|.*-->$",i)
        if x:
            n=len(i)
            print("Single line comment:\n",i[4:n-4])
        elif y:
            string+=i
            n=len(i)
    print("Multi line comment:\n",string[4:n-3])
single_multi()
        
