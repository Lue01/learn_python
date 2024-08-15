class Phone:
    IMEI=None
    producer='ITCAST'
    
    def call_by_5g(self):
        print("父类的5g通话")
        
class MyPhone(Phone):
    producer="ITHEIMA"
    
    def call_by_5g(self):
        print("子类的5g通话")
        print(super().producer)
    
phone=MyPhone()
phone.call_by_5g()
print(phone.producer)
