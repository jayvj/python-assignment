import json
with open("in_4.json","r")as f:
    dic=json.load(f)
dic["dic1"]["Month"]="October"
dic["dic2"]["Month"]="November"
dic["dic3"]["Month"]="January"
dic["dic4"]["Month"]="November"
dic["dic5"]["Month"]="October"
#print(dic)
def Month(z):
    count=0
    for k in dic:
        if dic[k].get("Month")==z:
            count=count+1
    print(z,(count))
Month("October")
Month("November")
Month("January")
        
