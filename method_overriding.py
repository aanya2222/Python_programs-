from math import pi
class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        return self.l*self.b
    
class circle:
    def __init__(self,r):
        self.r=r
        
    def area(self):
        return pi*self.r*2*2
    

r1=rect(5,3)
c1=circle(10)
print("Area of rect",r1.area())
print("Area of circle",c1.area())
for common in (r1,c1):
    print("Area is",common.area())

        