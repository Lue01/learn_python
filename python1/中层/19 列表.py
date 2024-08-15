name=['itheima',666,True,[1,2,3]]
print(name)
print(type(name))
print(name[0])
print(name[1])
print(name[2])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[3][1])
# 查找指定元素的位置
index=name.index(666)
print(index)

name[0]="中国"
print(name)
# 指定位置插入
name.insert(2,456)
print(name)
# 尾部插入一个元素
name.append("the one")
print(name)
# 尾部插入多个元素
name.extend([456,5,10])
print(name)
# 统计某元素在列表中的个数
print(name.count(456))
# 删除指定位置元素
del name[-2]
print(name)
elelment=name.pop(-1)
print(name)
print(elelment)
# 删除指定元素的第一个匹配项
name.remove(456)
print(name)
# 统计列表中所有元素个数
length=len(name)
print(length)
# 清空列表
name.clear()
print(name)

