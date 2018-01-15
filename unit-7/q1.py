import re
class introman:
    def int_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val


try:
	fi=open("ipfileq1.txt","r+")
	fi.seek(0,0)
	print ("\nInput file:")
	for val in fi.readlines():
		ele=val.strip("\n")
		print (ele)
	fi.seek(0,0)
	print ("\nOutput file:")
	for val in fi.readlines():
		ele=val.strip("\n")
		num=re.search(r'\d+',ele,re.M)
		if num:
			integer=int(ele)
			print (introman().int_to_roman(integer))
		else:
			roman=str(ele)
			print (introman().roman_to_int(roman))
	

except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nConverting an integer to a roman numeral and vice versa is executed successfully!")

	
finally:
	print ("\nFinished.\n")
