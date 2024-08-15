# 函数的多返回值
from asyncio import gather

from flask import g


def test_return():
    return 1,2

x,y=test_return()
print(x)
print(y)

def user_info(name,age,gender):
    print(f'你的名字是{name}，年龄是{age}，性别是{gender}')
    
user_info('TOM',20,'男')

user_info(age=52,gender='nv',name='小红')

# 不定长，作为元组
def user(*args):
    print(args)
    
user('小李','女')

#不定长，作为字典
def user2(**kwargs):
    print(kwargs)
    
user2(name='小刚',age=13)

# 将函数当成参数传入
def test(compute):
    result=compute(1,2)
    print(result)
    
def compute(x,y):
    return x+y

test(compute)