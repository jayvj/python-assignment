class Complex:

       def input(self,a,b,c,d):
          self.a=a
          self.b=b
          self.c=c
          self.d=d

       def printno(self):
          self.c1=complex(self.a,self.b)
          self.c2=complex(self.c,self.d)
          print "\nThe complex numbers are:",self.c1," and ",self.c2

       def addno(self):
          self.cadd=self.c1+self.c2
          print "\nAddition:"
          if self.cadd.imag>0:
            print round(self.cadd.real,2),"+",round(self.cadd.imag,2),"i"
          else:
            print round(self.cadd.real,2),round(self.cadd.imag,2),"i"

       def subno(self):
          self.csub=self.c1-self.c2
          print "\nSubtraction:"
          if self.csub.imag>0:
            print round(self.csub.real,2),"+",round(self.csub.imag,2),"i"
          else:
            print round(self.csub.real,2),round(self.csub.imag,2),"i"

       def mulno(self):
          self.cmul=self.c1*self.c2
          print "\nMultiplication:"
          if self.cmul.imag>0:
            print round(self.cmul.real,2),"+",round(self.cmul.imag,2),"i"
          else:
            print round(self.cmul.real,2),round(self.cmul.imag,2),"i"

       def divno(self):
          self.cdiv=self.c1/self.c2
          print "\nDivision:"
          if self.cdiv.imag>0:
            print round(self.cdiv.real,2),"+",round(self.cdiv.imag,2),"i"
          else:
            print round(self.cdiv.real,2),round(self.cdiv.imag,2),"i"

       def modno(self):
          self.mod1=abs(self.c1)
          print "\nModulus:"
          print "Mod1:"
          print round(self.mod1,2),"+0.00i"
          self.mod2=abs(self.c2)
          print "Mod2:"
          print round(self.mod2,2),"+0.00i"


try:
	c=Complex()
	c.input(4,2,1,3)
	c.printno()
	c.addno()
	c.subno()
	c.mulno()
	c.divno()
	c.modno()


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrinting the result of their addition, subtraction, multiplication, division and modulus operations and the real and imaginary precision part should be correct up to two decimal places is executed successfully!")

	
finally:
	print ("\nFinished.\n")
