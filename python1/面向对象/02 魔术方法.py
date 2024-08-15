
class student:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
    def __str__(self) -> str:
        return (f"name:{self.name},age:{self.age}")
    
    def __lt__(self,other):
        return self.age<other.age
    
    def __le__(self,other):
        return self.age<=other.age
    
    def __eq__(self,other):
        return self.age==other.age
    
stu1=student("张三",15)
stu2=student("李四",16)
print(stu1)
print(str(stu1))

print(stu1<stu2)
print(stu1>stu2)