print(f"My name is {__name__}")

class A:
    def __init__(self):
        print("A Constructor")

    def x1(self):
        print(f"A-x1, self = {self}, super = {super()}")

    def x3(self):
        print(f"A - x3, self = {self}, super = {super()}")
        print(self.T)

class B(A):
    def x1(self):
         print(f"B-x1, self = {self}, super = {super()}") 
         super().x1()

    def x2(self):
        print(f"B - x2, self = {self}, super = {super()}")
        super().x3()

class C(A):
    def x1(self):
        print(f"C-x1, self = {self}, super = {super()}")  
        #super(C,self).x1()
    def xx1(self):
        print(f"C-xx1")

    def x2(self):
        print(f"C - x2")
        super().x2()
    def x3(self):
        print(f"C - x3")

class D(B,C):
    def x12(self):
        print(f"D-x1, self = {self}, super = {super()}")  
        super(B,self).x1()

print(D.__mro__)
D().x1() # in this case it invoke x1 method of C after B instead as it could firstly appear (because B.x1() super().x1 so seems it call A.x1 if we call directly B.x1)



