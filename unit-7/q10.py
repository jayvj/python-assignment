import math

class points:
	def __init__(self,i,j,k):
		self.a=i;
		self.b=j;
		self.c=k;

class angle:
	def __init__(self,A1,B1,C1,D1):
		print ("\nAngle between the plane made by the points A, B, C and B, C, D in degrees(not radians):")
		AB=self.AB=points(0,0,0)
		BC=self.BC=points(0,0,0)
		CD=self.CD=points(0,0,0)
		ABBC=self.ABBC=points(0,0,0)
		BCCD=self.BCCD=points(0,0,0)
		A=self.A=A1
		B=self.B=B1
		C=self.C=C1
		D=self.D=D1 
		AB.a=B.a-A.a
		AB.b=B.b-A.b
		AB.c=B.c-A.c
		BC.a=C.a-B.a
		BC.b=C.b-B.b
		BC.c=C.c-B.c
		CD.a=D.a-C.a
		CD.b=D.b-C.b
		CD.c=D.c-C.c
		ABBC.a=(AB.b*BC.c)-(BC.b*AB.c)
		ABBC.b=(BC.a*AB.c)-(AB.a*BC.c)
		ABBC.c=(AB.a*BC.b)-(BC.a*AB.b)
		BCCD.a=(BC.b*CD.c)-(CD.b*BC.c)
		BCCD.b=(CD.a*BC.c)-(BC.a*CD.c)
		BCCD.c=(BC.a*CD.b)-(CD.a*BC.b)
		numerator=(ABBC.a*BCCD.a)+(ABBC.b*BCCD.b)+(ABBC.c*BCCD.c)
		mod_x=math.sqrt((ABBC.a*ABBC.a)+(ABBC.b*ABBC.b)+(ABBC.c*ABBC.c))
		mod_y=math.sqrt((BCCD.a*BCCD.a)+(BCCD.b*BCCD.b)+(BCCD.c*BCCD.c))
		denominator=mod_x*mod_y
		angle=numerator/denominator
		ans=math.degrees(math.acos(angle))
		print ("%.2f"%(ans))

		
try:
	A=points(2,4,3)
	B=points(1,7,5)
	C=points(2,1,5)
	D=points(1,4,5)
	l=angle(A,B,C,D)


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nPrinting the angle between the plane made by the points A, B, C and B, C, D in degrees(not radians) is executed successfully!")

	
finally:
	print ("\nFinished.\n")
