import json
with open("in_4.json","r+")as f:
    dic=json.load(f)
def Activity1():
    while True:
        print("\n")
        print("**Press x to exit**")
        print("Scientists in dic:\nAPJ ABDUL KALAM\nC.V.RAMAN\nBENJAMIN FRANKLIN\nALBERT EINSTIEN\nSIR ISAC NEWTON")
        tell=raw_input("Tell the sci_name whose bday is to be printed?")
        if tell=="APJ ABDUL KALAM":
            print(dic["dic1"]["D.O.B"])
        elif tell=="C.V.RAMAN":
            print(dic["dic2"]["D.O.B"])
        elif tell=="BENJAMIN FRANKLIN":
            print(dic["dic3"]["D.O.B"])
        elif tell=="ALBERT EINSTEIN":
            print(dic["dic4"]["D.O.B"])
        elif tell=="SIR ISAC NEWTON":
            print(dic["dic5"]["D.O.B"])
        elif tell=="x":
            break;
        else:
            print("No data found in Dictionary..!")
Activity1()
print("\n")
print("It's Time to update your dic..!")
print("**Press x to exit**")
new_name=raw_input("Enter the Scientists full name:")
new_dob=raw_input("Enter the Scientists D.O.B:")
dic["dic6"].update({"Sci_3:":new_name,"D.O.B":new_dob})
print("Updated dic:\n",dic)
with open("out_4.json","w")as file:
    json.dump(dic,file)

