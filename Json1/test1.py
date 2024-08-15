""" 
写一个python脚本，使用递归从目录下找到
所有指定后缀的文件，读取内容，按要求转换为json，
存储到根目录的content.json中。
"""

import os
import json

unique_students={}

# 首先定义一个函数用来递归查找目录下指定后缀的文件
def find_file(direct,suffix,universities):
    """递归查找指定后缀的文件

    Args:
        dict (_type_):当前目录
        suffix (_type_): 文件后缀
        files_list (_type_): 存储文件的列表
    """
    for item in os.listdir(direct):
        # 文件的完整路径
       
        item_path=os.path.join(direct,item)
        
        # 如果是文件而且后缀匹配
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            # 读取文件内容
            with open(item_path,"r",encoding="UTF-8") as file:
                for line in file:
                   parts=line.strip().split()
                   
                   if len(parts)==5:
                       student_name,university_name,enrollment_year,gaokao_score,major=parts
                       
                       enrollment_year=int(enrollment_year)
                       gaokao_score=int(gaokao_score)
                       
                       if gaokao_score<550:
                           continue
                       
                       unique_key=(student_name,university_name,enrollment_year,gaokao_score,major)
                       
                       if unique_key not in unique_students:
                           unique_students[unique_key]={
                               'student_name':student_name,
                               'university_name':university_name,
                               'enrollment_year':enrollment_year,
                               'gaokao_score':gaokao_score,
                               'major':major
                           }
                
                
                for key,student in unique_students.items():       
                       found=False
                       for uni in universities:
                           if uni['university_name']==student['university_name']:
                               uni['students'].append(student)
                               found=True
                               break
                        
                       if not found:
                           universities.append({
                               'university_name':student['university_name'],
                               'students':[student]
                           })
                            
                       
         
         # 如果是目录   
        elif os.path.isdir(item_path):
            find_file(item_path,suffix,universities)
            

def main():
    universities=[]
   

    
    search_direct="C:\\Python\\files"
    
    file_suffix='.log'
    
    find_file(search_direct,file_suffix,universities)
    
    with open('content.json','w',encoding='UTF-8') as json_file:
        json.dump(universities,json_file,ensure_ascii=False,indent=4)
        
main()
                
        
#需要用循环读取所有文件的内容

#将读取的内容转换为json

#存储到根目录