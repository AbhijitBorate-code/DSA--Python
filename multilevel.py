class personal:

    def __init__(self,name):
        self.name =name

    def show1(self):
        return self.name

class Details(personal):

    def __init__(self,name,age):
        personal.__init__(self,name)
        self.age=age

    def show2(self):
        return self.age

class info(Details):

    def __init__(self,name,age ,education):
        personal.__init__(self,name)
        Details.__init__(self,name ,age)
        self.education =education

    def show3(self):
        return self.education


s = info("Abhijt",12,"Enginarring")
print(s.show1())
print(s.show2())
print(s.show3())
