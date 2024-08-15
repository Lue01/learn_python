# 字符串模块


# 将输入字符串反转
def str_reverse(s):
    return s[::-1]

def substr(s,x,y):
    """_summary_
    将输入字符串按给定的两个下标进行切片
    Args:
        s (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
    """
    return s[x:y:1]

if __name__=='__main__':
    print(str_reverse("wuhan"))
    print(substr("中国武汉",1,3))