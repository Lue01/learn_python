import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts


# 美国的数据
f_us=open("C:\\itheima\\美国.txt","r",encoding="utf-8")
us_data=f_us.read()
us_data=us_data[us_data.find('{'):us_data.rfind('}')+1]
# us_data=us_data.replace("jsonp_1629344292311_69436(","")
# us_data=us_data[:-2]

us_dict=json.loads(us_data)

us_trend_data=us_dict['data'][0]['trend']

us_x_data=us_trend_data['updateDate'][:314]
us_y_data=us_trend_data['list'][0]['data'][:314]

# 日本的数据
f_rb=open("C:\\itheima\\日本.txt","r",encoding="utf-8")
rb_data=f_rb.read()
rb_data=rb_data[rb_data.find('{'):rb_data.rfind('}')+1]
rb_dict=json.loads(rb_data)

rb_trend_data=rb_dict['data'][0]['trend']

rb_x_data=rb_trend_data['updateDate'][:314]
rb_y_data=rb_trend_data['list'][0]['data'][:314]

# 印度的数据
f_yd=open("C:\\itheima\\印度.txt","r",encoding="utf-8")
yd_data=f_yd.read()
yd_data=yd_data[yd_data.find('{'):yd_data.rfind('}')+1]
yd_dict=json.loads(yd_data)

yd_trend_data=yd_dict['data'][0]['trend']

yd_x_data=yd_trend_data['updateDate'][:314]
yd_y_data=yd_trend_data['list'][0]['data'][:314]

# 构建图表
line=Line()
line.add_xaxis(us_x_data)  # x轴是公用的
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",rb_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",yd_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数折线图",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),     #示例
    toolbox_opts=ToolboxOpts(is_show=True),   # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True)  # 视觉映射
    
)

line.render()

f_us.close()
f_rb.close()
f_yd.close()
