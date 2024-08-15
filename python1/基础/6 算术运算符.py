print("1+1=",1+1)
print("1-1=",1-1)
print("1*1=",1*1)
print("4/2=",4/2)
print("4//3=",4//3)
print("9%2=",9%2)
print("2**2=",2**2)

num=1+2*3

num+=1
num-=1

#字符串的拼接，字符串不能与整型直接拼接
name="黑马"
number=1456
print("我叫" + name + "，我的电话是"+str(number))

#字符串格式化
print("我叫%s,我的电话是%s"%(name,number))

price=19.99
print("我叫%s，我的电话号码是%d，我买了%6.2f的衬衫"%(name,number,price))