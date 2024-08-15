# 键是唯一的，最后一个会覆盖前面的；值可以重复
my_dict={}
my_dict=dict()
my_dict={"小刘":84,"小李":96,"小陈":60}
print(my_dict)
# 增加及更新
my_dict["小刘"]=88
my_dict["小石"]=51
print(my_dict)
# 删除
score=my_dict.pop("小陈")
print(my_dict)
print(score)
# 获取全部的key
keys=my_dict.keys()
print(keys)
# 遍历
for key in keys:
    print(my_dict[key])
for key in my_dict:
    print(my_dict[key])
# 统计
num=len(my_dict)
print(num)