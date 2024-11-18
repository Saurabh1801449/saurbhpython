class Parent1:
    def display(self):
        print("This is the parent1 class.")

class Parent2(Parent1):
    def display1(self):
        print("This is the parent2 class.")
        
class Child(Parent2):
    def display2(self):
        print("This is the child class.")


child = Child()
child.display()   
child.display1()  
child.display2()  
