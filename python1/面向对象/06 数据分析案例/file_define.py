from date_define import Record
import json

class FileReader:
    def read_data(self) -> list[Record]:
        pass
    
    
class TextFileReader(FileReader):
    def __init__(self,path) -> None:
        self.path=path
        
    def read_data(self) -> list[Record]:
        f=open(self.path,'r',encoding='utf-8')
        record_list=[]
        
        for line in f.readlines():
            line=line.strip()   #去除回车符
            data_list=line.split(",")
            record=Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        
        f.close()    
        return record_list
    
    
class JsonFileReader(FileReader):
    def __init__(self,path) -> None:
        self.path=path
        
    def read_data(self) -> list[Record]:
        f=open(self.path,'r',encoding='utf-8')
        record_list=[]
        
        for line in f.readlines():
            data_dict=json.loads(line)
            record=Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
            
        f.close()
        return record_list    
    
            
if __name__ == '__main__':
    text_file_reader=TextFileReader("C:\\itheima\\2011年1月销售数据.txt")
    json_file_reader=JsonFileReader("C:/itheima/2011年2月销售数据JSON.txt")
    
    list1=text_file_reader.read_data()
    list2=json_file_reader.read_data()
    
    for l in list1:
        print(l)
        
    for l in list2:
        print(l)