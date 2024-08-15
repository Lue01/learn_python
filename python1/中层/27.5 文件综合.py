f1=open("C:\\Python\\test.txt","r","encoding=utf-8")

f2=open("C:\\Python\\test.txt.bak","w",encoding="UTF-8")

for line in f1:
    if "测试" in line:
        continue
    f2.write(line)
    
f1.close()
f2.close()