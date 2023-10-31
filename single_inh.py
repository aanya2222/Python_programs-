class student:
    def input(self, name, roll, PNR, address):
        self.name = name
        self.roll = roll
        self.PNR = PNR
        self.address = address
        
    def display(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("PNR: ", self.PNR)
        print("Address: ", self.address)
        
class CSE(student):
    def setMarks(self, marks):
        self.marks = marks
        
    def setSubject(self, subject):
        self.subject = subject
        
    def display(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("PNR: ", self.PNR)
        print("Address: ", self.address)
        print("Marks: ", self.marks)
        print("Subject: ", self.subject)
        

s1 = CSE()
s1.input("Neeta", 36, 'EN21195219', 'Kolhapur')
s1.setMarks(500)
s1.setSubject("Python")
s1.display()
       