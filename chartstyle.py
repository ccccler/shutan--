class Chart:

    class Scatter:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

c = (
    Scatter(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-显示分割线"),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
    )
    .render("scatter_splitline.html")
)

        '''

    class Bar:
        ex_data = '''{'月份':['1月','2月','3月','4月'],'水量':[2938,2909,1292,3341]}'''

        ex_code = '''```
        from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

# infographic主题
c = (
    # 该行设置主题
    Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True)
    )
    # 该行设置线
    .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(y=50, name="yAxis=50")]
            ))
    .render("bar.html")
)


        '''

    class Bar_Stack:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

list2 = [
    {"value": 12, "percent": 12 / (12 + 3)},
    {"value": 23, "percent": 23 / (23 + 21)},
    {"value": 33, "percent": 33 / (33 + 5)},
    {"value": 3, "percent": 3 / (3 + 52)},
    {"value": 33, "percent": 33 / (33 + 43)},
]

list3 = [
    {"value": 3, "percent": 3 / (12 + 3)},
    {"value": 21, "percent": 21 / (23 + 21)},
    {"value": 5, "percent": 5 / (33 + 5)},
    {"value": 52, "percent": 52 / (3 + 52)},
    {"value": 43, "percent": 43 / (33 + 43)},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis([1, 2, 3, 4, 5])
    .add_yaxis("product1", list2, stack="stack1", category_gap="50%")
    .add_yaxis("product2", list3, stack="stack1", category_gap="50%")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="middle",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
            background_color="#FFFFFF"
        ))
    .render("stack_bar_percent.html")
)

        '''

    class Bar_x:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_dataset(
        source=[
            ["score", "amount", "product"],
            [89.3, 58212, "Matcha Latte"],
            [57.1, 78254, "Milk Tea"],
            [74.4, 41032, "Cheese Cocoa"],
            [50.1, 12755, "Cheese Brownie"],
            [89.7, 20145, "Matcha Cocoa"],
            [68.1, 79146, "Tea"],
            [19.6, 91852, "Orange Juice"],
            [10.6, 101852, "Lemon Juice"],
            [32.7, 20112, "Walnut Brownie"],
        ]
    )
    .add_yaxis(
        series_name="",
        y_axis=[],
        encode={"x": "amount", "y": "product"},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Dataset normal bar example"),
        xaxis_opts=opts.AxisOpts(name="amount"),
        yaxis_opts=opts.AxisOpts(type_="category"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True),
        visualmap_opts=opts.VisualMapOpts(
            orient="horizontal",
            pos_left="center",
            min_=10,
            max_=100,
            range_text=["High Score", "Low Score"],
            dimension=0,
            range_color=["#D7DA8B", "#E15457"],

        ),
    )
    .render("dataset_bar_1.html")
)

        '''

    class Box_plot:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Boxplot
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

v1 = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
]
v2 = [
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
]

c = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
c.add_xaxis(["expr1", "expr2"])
c.add_yaxis("A", c.prepare_data(v1))
c.add_yaxis("B", c.prepare_data(v2))
c.set_global_opts(
    title_opts=opts.TitleOpts(title="这里放置标题"),
    toolbox_opts=opts.ToolboxOpts(),
    legend_opts=opts.LegendOpts(is_show=False)
)
c.render("boxplot_base.html")


        '''

    class Calender:
        ex_code='''```
        import random
import datetime
import pyecharts.options as opts
from pyecharts.charts import Calendar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

(
    Calendar()
    .add(
        series_name="",
        yaxis_data=data,
        calendar_opts=opts.CalendarOpts(
            pos_top="120",
            pos_left="30",
            pos_right="30",
            range_="2017",
            yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2017年步数情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000, min_=500, orient="horizontal", is_piecewise=False,
        ),
    )
    .render("calendar_heatmap.html")
)

        '''

    class Funnel:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker

c = (
    Funnel()
    .add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"),
                     toolbox_opts=opts.ToolboxOpts(),
                     legend_opts=opts.LegendOpts(is_show=True)
                     )
    .render("funnel_base.html")
)

        '''

    class K_line:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Kline

data = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    [2360.75, 2382.48, 2347.89, 2383.76],
    [2383.43, 2385.42, 2371.23, 2391.82],
    [2377.41, 2419.02, 2369.57, 2421.15],
    [2425.92, 2428.15, 2417.58, 2440.38],
    [2411, 2433.13, 2403.3, 2437.42],
    [2432.68, 2334.48, 2427.7, 2441.73],
    [2430.69, 2418.53, 2394.22, 2433.89],
]


c = (
    Kline() 
    .add_xaxis(["2017/7/{}".format(i + 1) for i in range(12)])
    .add_yaxis("kline", data)
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(is_scale=True),
        xaxis_opts=opts.AxisOpts(is_scale=True),
        title_opts=opts.TitleOpts(title="Kline-基本示例"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .render("kline_base.html")
)

        '''

    class Line:
        ex_data = '''
        Mon  Tue  Wed  Thu  Fri  Sat  Sun
        150  230  224  218  135  147  260
        '''

        ex_code = '''```
        import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType


x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_data = [820, 932, 901, 934, 1290, 1330, 1320]


(
    Line(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="邮件营销",
        stack="总量",
        y_axis=[120, 132, 101, 134, 90, 230, 210],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="直接访问",
        stack="总量",
        y_axis=[320, 332, 301, 334, 390, 330, 320],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="搜索引擎",
        stack="总量",
        y_axis=[820, 932, 901, 934, 1290, 1330, 1320],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="折线图堆叠"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True)
    )
    .render("line_chart.html")
)

        '''

    class Line_area:
        ex_code='''```
        import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


c = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), is_smooth=True)
    .add_yaxis("商家B", Faker.values(), is_smooth=True)
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Line-面积图（紧贴 Y 轴）"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
    .render("line_areastyle.html")
)

        '''

    class Pie:
        ex_code='''```
        from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())],rosetype="rosetype",)
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"),
                     toolbox_opts=opts.ToolboxOpts(),
                     legend_opts=opts.LegendOpts(is_show=True)
                     )

    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
)

        '''

    def __getattr__(self, name):
        # 尝试从 Chart 类中获取与 name 同名的类
        try:
            return getattr(self.__class__, name.capitalize())
        except AttributeError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")