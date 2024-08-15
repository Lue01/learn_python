import random
num=random.randint(1,10)
guess=int(input("请进行第一次猜测："))
if int(guess)==num:
    print("Yes")
else:
    if guess>num:
        print("Big")
    else:
        print("Small")
    guess=int(input("请进行第二次猜测：") )
    if int(guess)==num:
        print("Yes")
    else:
        if guess>num:
            print("Big")
        else:
            print("Small")
        guess=int(input("请输入第三次猜测："))
        if guess==num:
            print("Yes")
        else:
            print("No") 
    