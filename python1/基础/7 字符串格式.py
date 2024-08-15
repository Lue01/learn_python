#字符串的拼接，字符串不能与整型直接拼接
name="黑马"
number=1456
print("我叫" + name + "，我的电话是"+str(number))

#字符串格式化
print("我叫%s,我的电话是%s"%(name,number))

price=19.99
print("我叫%s，我的电话号码是%d，我买了%6.2f的衬衫"%(name,number,price))


# 通过语法f"内容{变量}"来快速格式化
print(f"我叫{name}，我的电话号码是{number}，我买了一件{price}的衬衫t'r'w'r")