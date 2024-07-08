class Student:
    def __init__(self,name,marks):
         self.name = name
         self.marks = marks

    def display(self):
        total = 0
        for value in self.marks:
            total = value + total
        print(self.name + " Has scored " + str(total/3))

s1 = Student("neo",[90,80,90])
s1.display()

