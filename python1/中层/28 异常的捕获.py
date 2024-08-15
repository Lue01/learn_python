try:
    f=open("C:\\Python\\abc","r",encoding="UTF-8")
except Exception:
    print("出现异常")
    f=open("C:\\Python\\abc","w",encoding="UTF-8")
else:
    print("未出现异常")
finally:
    print("不管出没出现异常")
    f.close()