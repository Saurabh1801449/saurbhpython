class State:
    def Capital(self):
        pass
    
class Maharashtra(State):
    def Capital(self):
        print("Mumbai")
    
class Karnataka(State):
    def Capital(self):
        print("Bangalore")
        
Mh = Maharashtra()
Kn = Karnataka()

Mh.Capital()
Kn.Capital()