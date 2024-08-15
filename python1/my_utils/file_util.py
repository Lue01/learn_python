# 文件处理模块

def print_file_info(file_name):
    """_summary_
    接收传入文件的路径，打印文件全部内容，如果文件不存在则捕获异常，输出提示信息，
    通过finally关闭文件对象

    Args:
        file_name (_type_): _description_
    """
    f=None
    try:
        f=open(file_name,'r',encoding='utf-8')
        content=f.read()
        print("正在打印文件内容:")
        print(content)
    except Exception as e:
        print(f"程序出现如下异常：{e}")
    finally:
        # 如果文件为空，f.close会出错，因此进行判断，f为none则为false
        if f:
            f.close()
        
def append_to_file(file_name,data):
    """
    将传入的数据写入传入的文件中

    Args:
        file_name (_type_): _description_
        data (_type_): _description_
    """
    f=open(file_name,'a',encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.close()