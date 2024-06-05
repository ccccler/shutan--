from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

data = [
    ("农、林、牧、渔业", 62952), ("采矿业", 135025), ("制造业", 103932),
    ("电力、热力、燃气及水生产和供应业", 143594), ("建筑业", 85804),
    ("批发和零售业", 124362), ("交通运输、仓储和邮政业", 122705),
    ("住宿和餐饮业", 58094), ("信息传输、软件和信息技术服务业", 231810),
    ("金融业", 197663), ("房地产业", 91932), ("租赁和商务服务业", 109264),
    ("科学研究和技术服务业", 171447), ("水利、环境和公共设施管理业", 68656),
    ("居民服务、修理和其他服务业", 68919), ("教育", 124067),
    ("卫生和社会工作", 143818), ("文化、体育和娱乐业", 127334),
    ("公共管理、社会保障和社会组织", 117108)
]
data.sort(key=lambda x: x[1], reverse=True)
x_data = [x[0] for x in data[:5]]
y_data = [x[1] for x in data[:5]]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(x_data)
    .add_yaxis("行业平均工资", y_data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="行业平均工资最高的5个行业", subtitle="2023年数据"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True)
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(y=120698, name="总平均工资")]
        ))
    .render("添加分析.html")
)