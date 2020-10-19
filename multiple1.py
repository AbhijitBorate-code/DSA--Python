"""class person:

    def __init__(self,name):
        self.name =name

    def show(self):
        return self.name

class father:

    def __init__(self,age):
       # person.__init__(self,name)
        self.age=age

    def show1(self):
        return self.age

class son(person,father):

    def __init__(self,name,age,birthdate):
        person.__init__(self,age)
        father.__init__(self,name)
        self.birthdate =birthdate

    def show3(self):
        return self.birthdate


s =son("Abhijt",12,3-71010)
print(s.show() )
print(s.show1())
print(s.show3())"""


class person:
    name = ""

    def show(self):
        return self.name

class Detail:
    age =""

    def show1(self):
        return self.age

class Info(person,Detail):

    def show2(self):
        print("personal",self.name)
        print("Details",self.age)

s =Info()
s.name ="Abhijit"
s.age =12
s.show1()
s.show2()
print(s.show2())