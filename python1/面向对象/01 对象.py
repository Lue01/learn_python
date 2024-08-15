class student:
    def __init__(self) -> None:
        self.name=input("请输入学生姓名：")
        self.age=input("请输入学生年龄：")
        self.location=input("请输入学生地址：")
        print(f"学生姓名：{self.name},年龄：{self.age}，地址：{self.location}")
stu=[]
for i in range(0,10):     
    stu[i]=student()