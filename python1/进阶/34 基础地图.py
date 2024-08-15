from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map=Map()

data=[
    ("北京市",99),
    ("上海市",199),
    ("广东省",145),
    ("湖北省",283),
]

map.add("测试地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True)
)

map.render()