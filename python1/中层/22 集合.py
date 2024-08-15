# 集合无序不重复,允许修改
name=set()
name={"中国","湖北","武汉","中国","湖北","武汉","中国","湖北","武汉"}
print(name)

name.add("python")
print(name)

name.remove("中国")
print(name)
# 随机取出一个元素
element=name.pop()
print(element)

# name.clear()
# print(name)
# 取两个集合之间的差集
name2={"中国"}
name3=name.difference(name2)
print(name)
print(name2)
print(name3)
# 消除两个集合的差集(在集合1内删除和集合2相同的元素)
name.difference_update(name2)
print(name)
# 组合成新集合
name4=name.union(name2)
print(name4)
