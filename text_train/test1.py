

import json  
  
# 打开原始文件并读取内容  
with open("C:\\Users\\Secrecy\\Downloads\\train.txt", 'r', encoding='utf-8') as file:  
    # 读取整个文件内容到一个字符串中  
    content = file.read()  
  
    contents = []  
    lines = content.splitlines()  # 将整个文件内容按行分割  
    for line in lines:  
        try:  
            # 尝试解析每一行作为JSON对象  
            data = json.loads(line)  
            # 提取content字段的值  
            contents.append(data['content'])  
        except json.JSONDecodeError:  
            # 如果解析失败（可能是因为该行不是一个完整的JSON对象），则忽略它  
            # 注意：在实际应用中，你可能需要更复杂的错误处理逻辑  
            pass  
  
# 将提取的content写入到新文件中  
with open('extracted_contents.txt', 'w', encoding='utf-8') as file:  
    for content in contents:  
        file.write(content + '\n')  
  
print("内容已提取并保存到extracted_contents.txt文件中。")