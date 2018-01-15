class Rectangle():    
	def rectangle_area(self,length,width):
		return length*width
	
	def rectangle_perimeter(self,length,width):
		return 2*(length+width)

class Circle():    
	def circle_area(self,radius):
		return 3.14*radius*radius
	
	def circle_perimeter(self,radius):
		return 2*3.14*radius

class Triangle():    
	def triangle_area(self,base,height):
		return 0.5*base*height
	
	def triangle_perimeter(self,a,b,c):
		return a+b+c

class Rhombus():    
	def rhombus_area(self,base,height):
		return base*height
	
	def rhombus_perimeter(self,side):
		return 4*side

class Pentagon():    
	def pentagon_area(self,side,apothem_length):
		return 2.5*side*apothem_length
	
	def pentagon_perimeter(self,side):
		return 5*side


try:
	fo=open("opfileq8.txt","r+")
	fo.seek(0,0)
	fo.truncate()
	print ("\nRECTANGLE:")
	length=float(input("Enter length: "))
	width=float(input("Enter width: "))
	recarea=Rectangle().rectangle_area(length,width)
	recperi=Rectangle().rectangle_perimeter(length,width)
	print ("Area of a rectangle: %.2f sq.units"%recarea)
	print ("Perimeter of a rectangle: %.2f units"%recperi)
	fo.write("Area of a rectangle: "+str(recarea))
	fo.write("\nPerimeter of a rectangle: "+str(recperi))


	print ("\nCIRCLE:")
	radius=float(input("Enter radius: "))
	cirarea=Circle().circle_area(radius)
	cirperi=Circle().circle_perimeter(radius)
	print ("Area of a circle: %.2f sq.units"%cirarea)
	print ("Perimeter of a circle: %.2f units"%cirperi)
	fo.write("\n\nArea of a circle: "+str(cirarea))
	fo.write("\nPerimeter of a circle: "+str(cirperi))

	
	print ("\nTRIANGLE:")
	a=float(input("Enter side a: "))
	b=float(input("Enter side b: "))
	c=float(input("Enter side c: "))
	base=float(input("Enter base: "))
	height=float(input("Enter height: "))
	triarea=Triangle().triangle_area(base,height)
	triperi=Triangle().triangle_perimeter(a,b,c)
	print ("Area of a triangle: %.2f sq.units"%triarea)
	print ("Perimeter of a triangle: %.2f units"%triperi)
	fo.write("\n\nArea of a triangle: "+str(triarea))
	fo.write("\nPerimeter of a triangle: "+str(triperi))


	print ("\nRHOMBUS:")
	side=float(input("Enter side: "))
	base=float(input("Enter base: "))
	height=float(input("Enter height: "))
	rhomarea=Rhombus().rhombus_area(base,height)
	rhomperi=Rhombus().rhombus_perimeter(side)
	print ("Area of a rhombus: %.2f sq.units"%rhomarea)
	print ("Perimeter of a rhombus: %.2f units"%rhomperi)
	fo.write("\n\nArea of a rhombus: "+str(rhomarea))
	fo.write("\nPerimeter of a rhombus: "+str(rhomperi))


	print ("\nPENTAGON:")
	side=float(input("Enter side: "))
	apothem_length=float(input("Enter apothem length: "))
	pentarea=Pentagon().pentagon_area(side,apothem_length)
	pentperi=Pentagon().pentagon_perimeter(side)
	print ("Area of a pentagon: %.2f sq.units"%pentarea)
	print ("Perimeter of a pentagon: %.2f units"%pentperi)
	fo.write("\n\nArea of a pentagon: "+str(pentarea))
	fo.write("\nPerimeter of a pentagon: "+str(pentperi))


except IOError:
	print ("\nAn error occured trying to read the file.")
except:
	print ("\nAn error occured.")


else:
	print ("\nArea and Perimeter of Rectangle, Circle, Triangle, Rhombus and Pentagon is executed successfully!")

	
finally:
	print ("\nFinished.\n")
