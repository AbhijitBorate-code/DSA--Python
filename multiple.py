# single inhritance using co0nstruction:


class person:

    def __init__(self,name , id):
        self.name =name
        self.id =id

   #""" def show(self):
    #    return(self.name)
     #   return(self.id)"""

class Employee(person):

    def __init__(self,name,id,salary ,post):
        person.__init__(self, name, id)
        self.salary = salary
        self.post=post



    def sho1(self):
        return(self.salary,self.post)



a =Employee("AHH",12303030,120000,"MD")
#print(a.show())
print(a.sho1())