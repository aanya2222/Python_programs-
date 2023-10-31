class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def display (self):
        print(self.name)
        print(self.id)

class emp(person):
    def __init__(self,name,id,salary,post): 
        self.salary=salary
        self.post=post
        person. __init__(self,name,id)
            
    def details(self):
        print("name", self.name)
        print("id", self.id)
        print("salary", self.salary)
        print("post", self.post)
        
a = emp("Neeta",10,20000,"developer")

a.display()
a.details()