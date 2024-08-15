count=10000
import random
for i in range(1,21):
    num=random.randint(1,10)
    if num<5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位。")
        continue
    else:
        if count==0:
            print("工资发完了，下个月再来吧")
            break
        count=count-1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{count}元")