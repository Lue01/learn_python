import json
data=[{"name":"小红","age":11},{"name":"小明","age":15},{"name":"小强","age":9}]
new_data=json.dumps(data,ensure_ascii=False)
print(type(new_data))
print(new_data)