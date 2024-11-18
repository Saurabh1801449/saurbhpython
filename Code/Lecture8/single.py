class Parent:
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    def display1(self):
        print("This is the child class.")

child = Child()
child.display()   
child.display1()  
