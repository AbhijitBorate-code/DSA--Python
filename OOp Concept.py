"""

# single Inheritance:

class student:

    def Details(self,roll, name):
        self.roll=roll
        self.name =name

    def show1(self):
        print(self.name,self.roll)


class Extra(student):

    def mail(self,mail_id):
            self.mail_id = mail_id

    def show(self):
            print(self.mail_id)


s1 =Extra()
s1.Details("Abhijt",12)
s1.show1()
s1.mail("abhijitborate@gmail.com")
s1.show()
"""



class Parents:
    def __init__(self,name):
        self.name= name


class Child(Parents):

    def __init__(self,name,child_name):
        Parents.__init__(self,name)
        self.child_name =child_name





s1 = Child("Dnyanoba ","Abhijt")
print(s1.name)
print(s1.child_name)
