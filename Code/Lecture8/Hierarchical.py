class Parent:
    def display(self):
        print("This is the parent class.")

        
class Child(Parent):
    def display1(self):
        print("This is the child class.")

class Child1(Parent):
    def display2(self):
        print("This is the child1 class.")


child = Child()
child.display()   
child.display1()   

child1 = Child1()
child1.display()   
child1.display2()  
