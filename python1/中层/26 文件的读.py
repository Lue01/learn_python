# 打开文件
f=open("C:\\Python\测试.txt","r",encoding="UTF-8")

# 读取文件,读取为字符串
# print(f.read(10)) //读取十个字
# print(f.read())  //全部读取

# 读取文件的全部行，封装到列表中
# line=f.readlines()
# print(line)
# 重点:每次读取都会在上一次读取的结束位置继续读取

# 循环读取文件行
# for line in f:
#     print(f"每一行的数据为：{line}")
    
# 文件的关闭
f.close()
import time 
time.sleep(2)   


with open("C:\\Python\测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)
