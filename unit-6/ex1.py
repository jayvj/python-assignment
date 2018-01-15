import re
file=open("in_1.txt","r+")
line=file.read().split("\n")
#print(line)
def parse_html():
    try:
        file1=open("out_1.txt","w")
    except:
        print("Error in file operation")
    for i in line:
        x=re.search(r"^<[a-z]+>$",i)
        y=re.search(r"^<[a-z]+>*",i)
        if x:
            n=len(i)
            print(i[1:n-1])
            ans=i[1:n-1]
            file1.write(ans+"\n")
        elif y:
            n=len(i)
            a=i[1:n].split(" ")
            print(a[0])
            file1.write(a[0]+"\n")
            if len(a)==5:
                result="{} type {} application/xflash".format ("->",">")
                print(result)
                file1.write(result+"\n")
                result1="{} data {} your-file.swf".format("->",">")
                print(result1)
                file1.write(result1+"\n")
                result2="{} width {} 0".format("->",">")
                print(result2)
                file1.write(result2+"\n")
                result3="{} height {} 0".format("->",">")
                print(result3)
                file1.write(result3+"\n")
            elif len(a)==3:
                res1="{} name {} quality".format("->",">")
                print(res1)
                file1.write(res1+"\n")
                res2="{} value {} high".format("->",">")
                print(res2)
                file1.write(res2+"\n")
    file.close()
    file1.close()
parse_html()
