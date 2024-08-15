i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

import random
num=random.randint(1,100)
count=1
guess=int(input("请输入猜测数字："))
while guess!=num:
    count=count+1
    if guess>num:
        print("Big")
    else:
        print("Small")
    guess=int(input("请输入猜测数字："))
print("一共猜了%d次"%count) 