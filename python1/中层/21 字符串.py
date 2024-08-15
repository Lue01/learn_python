# 移除首尾字符串
name="12itheima32"
new_name=name.strip("12")
print(new_name)
# 按给定字符串分割原字符串
name="i love china"
new_list=name.split(' ')
print(new_list)
# 替换指定字符串
new_name=name.replace("i","me")
print(new_name)
# 查找字符串
print(name.index("lo"))