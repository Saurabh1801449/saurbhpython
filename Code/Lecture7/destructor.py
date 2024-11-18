class dest:
    def __init__(self):
        print("Constructor called")
        
    def __del__(self):
        print("Destructor called")
        
    def create_obj(self):
        print("Object created")
        
obj = dest()
obj.create_obj()