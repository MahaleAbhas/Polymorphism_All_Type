#Duck Typing
class MIT:
    def BCA(self):
        print("BCA Brance In MIT")
    def MCA(self):
        print("MCA Brance In MIT")
    def BBA(self):
        print("BBA Brance In MIT")

class SPPU:
    def BCA(self):
        print("BCA Brance In SPPU")
    def MCA(self):
        print("BCA Brance In SPPU")
    def BBA(self):
        print("BCA Brance In SPPU")

def collg_info(col):
    col.BCA()
    col.MCA()
    col.BBA()

A=MIT()
B=SPPU()

collg_info(B)



#Method Overriding
class Circle:
    def area(self,r):
        ans=3.14*r*r
        print("Area of a circle:",ans)
class Square(Circle):
    def area(self,r):
        ans=r*r
        print("Area of the Square:",ans)

objsc=Square()
rr=int(input("Enter The Number:"))
objsc.area(rr)


#Method Overloading
from multipledispatch import dispatch
class Myclass:
    @dispatch(int,int)
    def add(self,a,b):
        ans=a+b
        print("Addition of two number:",ans)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        ans=a+b+c
        print("Addition Of two number:",ans)
        
obja=Myclass()
obja.add(10,20)
obja.add(10,20,30)


#Function Overloading
from multipledispatch import dispatch
@dispatch(int,int)
def mul(self,a,b):
    ans=a*b
    print("Multiplication of two number:",ans)

@dispatch(int,int,int)
def mul(self,a,b,c):
    ans=a*b*c
    print("Multiplication of three number:",ans)

add(10,20)
add(10,20,30)




































