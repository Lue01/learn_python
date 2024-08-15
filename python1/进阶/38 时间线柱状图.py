from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis() # 反转柱状图

bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,30,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis() # 反转柱状图

timeline=Timeline(
    {"theme":ThemeType.DARK}
)
timeline.add(bar1,"2021年GDP")
timeline.add(bar2,"2022年GDP")



timeline.add_schema(
    play_interval=1000,    # 自动播放的时间间隔
    is_timeline_show=True,  # 是否显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True # 是否循环自动播放
)


timeline.render("基础时间线柱状图.html")