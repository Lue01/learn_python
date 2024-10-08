import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts

f=open("C:\\itheima\\疫情.txt","r",encoding="utf-8")
data=f.read()
f.close()

data_dict=json.loads(data)

city_data_list=data_dict["areaTree"][0]["children"][3]["children"]

data_list=[]
for city_data in city_data_list:
    city_name=city_data["name"]+"市"
    city_confirm=city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm))

data_list.append(("济源市",5))
    
map=Map()

map.add("河南省疫情分布",data_list,"河南")

map.set_global_opts(
    title_opts=TitleOpts(title="河南疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1~99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100~999人","color":"#FFFF99"},
            {"min":1000,"max":9999,"label":"1000~9999人","color":"#FF9966"},
            {"min":10000,"max":99999,"label":"10000~99999人","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"}
        ]
    )
)

map.render("河南省疫情地图.html")