class Rectangle:
    def __init__(self,length=0,breadth=0):
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return "Length = %d breadth = %d"%(self.length,self.breadth)

    def __del__(self):
        del self.length
        del self.breadth

    def area(self):
        return self.length * self.breadth

    def setData(self,l=0,b=0):
        self.length = l
        self.breadth = b

    def inputData(self):
        self.length = int(input("Enter The Length : "))
        self.breadth = int(input("Enter The Breadth : "))

    def showData(self):
        print("The length is %d"%(self.length))
        print("The Breadth is %d"%(self.breadth))

    def __add__(self, other):
        l = self.length + other.length
        b = self.breadth + other.breadth
        return Rectangle(l,b)

    def __sub__(self, other):
        l = self.length - other.length
        b = self.breadth - other.breadth
        return Rectangle(l, b)

    def __mul__(self, other):
        l = self.length * other.length
        b = self.breadth * other.breadth
        return Rectangle(l, b)

    def __divmod__(self, other):
        l = self.length / other.length
        b = self.breadth / other.breadth
        return Rectangle(l, b)

    def __pow__(self, other):
        l = self.length ** other.length
        b = self.breadth ** other.breadth
        return Rectangle(l, b)

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

r1 = Rectangle(10,2)
r2 = Rectangle(3,3)
print(str(r1))
print(str(r2))
r3 = r1 + r2
print(str(r3))
if r2 <= r1:
    print("R2 is less than equal to R1")
else:
    print("R1 is less than equal to R2")