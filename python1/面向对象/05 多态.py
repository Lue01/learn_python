class AC:
    def cool_wind(self):
        pass
    
    def hot_wind(self):
        pass
    
    def swing(self):
        pass
    
class Midea(AC):
    def cool_wind(self):
        print("美的制冷")
        
    def hot_wind(self):
        print("美的加热")
        
    def swing(self):
        print("美的左右摆风")
        
class GREE(AC):
    def cool_wind(self):
        print("格力制冷")
        
    def hot_wind(self):
        print("格力加热")
        
    def swing(self):
        print("格力左右摆风")
        
def make_cool(ac:AC):
    ac.cool_wind()
    
midea=Midea()
gree=GREE()

make_cool(midea)
make_cool(gree)
    