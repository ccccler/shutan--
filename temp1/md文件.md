# 整理后的原始数据是：
年份	城镇非私营单位就业人员年平均工资	涨幅比率	行业分类	行业平均工资	行业工资增长率
2023	120698	5.8	总体	120698	5.8
2023	120698	5.8	农、林、牧、渔业	62952	6.7
2023	120698	5.8	采矿业	135025	11.1
2023	120698	5.8	制造业	103932	6.6
2023	120698	5.8	电力、热力、燃气及水生产和供应业	143594	8.0
2023	120698	5.8	建筑业	85804	9.6
2023	120698	5.8	批发和零售业	124362	7.8
2023	120698	5.8	交通运输、仓储和邮政业	122705	6.4
2023	120698	5.8	住宿和餐饮业	58094	7.6
2023	120698	5.8	信息传输、软件和信息技术服务业	231810	5.2
2023	120698	5.8	金融业	197663	13.4
2023	120698	5.8	房地产业	91932	1.8
2023	120698	5.8	租赁和商务服务业	109264	2.6
2023	120698	5.8	科学研究和技术服务业	171447	4.9
2023	120698	5.8	水利、环境和公共设施管理业	68656	0.6
2023	120698	5.8	居民服务、修理和其他服务业	68919	5.3
2023	120698	5.8	教育	124067	3.0
2023	120698	5.8	卫生和社会工作	143818	6.4
2023	120698	5.8	文化、体育和娱乐业	127334	5.1
2023	120698	5.8	公共管理、社会保障和社会组织	117108	-0.3
 # 该数据包含的主要维度：
{
          "维度1": {
            "name": "年份",
            "type": "int",
            "discription":"该属性描述了数据所在的年份"
          },
          "维度2": {
            "name": "城镇非私营单位就业人员年平均工资",
            "type": "float",
            "discription":"该属性描述了城镇非私营单位就业人员的年平均工资金额"
          },
          "维度3": {
            "name": "涨幅比率",
            "type": "float",
            "discription":"与前一年度相比工资增长的百分比"
          },
          "维度4": {
            "name": "行业分类",
            "type": "str",
            "discription":"该属性描述了不同行业的分类名称"
          },
          "维度5": {
            "name": "行业平均工资",
            "type": "float",
            "discription":"描述了在特定行业领域内的就业人员年平均工资金额"
          },
          "维度6": {
            "name": "行业工资增长率",
            "type": "float",
            "discription":"描述了特定行业内年平均工资同比增长的百分率"
          }
        }
# 以下是关于数据的分析与可视化：
## 分析1:随着时间的推移，城镇非私营单位就业人员的年平均工资增长趋势如何？
**涉及数据**：['年份', '城镇非私营单位就业人员年平均工资']
**解读**：2023年城镇非私营单位就业人员年平均工资增长5.8%，显示稳步上升趋势 
**可视化代码**：
```
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode

# 数据准备
years = ["2023"]
wages = [120698]
growth_rates = [5.8]
industries = ["总体", "农、林、牧、渔业", "采矿业", "制造业", "电力、热力、燃气及水生产和供应业", "建筑业",
              "批发和零售业", "交通运输、仓储和邮政业", "住宿和餐饮业", 
              "信息传输、软件和信息技术服务业", "金融业", "房地产业", 
              "租赁和商务服务业", "科学研究和技术服务业", "水利、环境和公共设施管理业", 
              "居民服务、修理和其他服务业", "教育", "卫生和社会工作", "文化、体育和娱乐业", "公共管理、社会保障和社会组织"]
industry_wages = [120698, 62952, 135025, 103932, 143594, 85804, 124362, 122705, 58094, 
                  231810, 197663, 91932, 109264, 171447, 68656, 68919, 
                  124067, 143818, 127334, 117108]

# 创建图表对象
line = Line(init_opts=opts.InitOpts(theme=None))

# 添加 X 轴数据
line.add_xaxis(xaxis_data=industries)

# 添加 Y 轴数据
line.add_yaxis(
    series_name="行业平均工资",
    y_axis=industry_wages,
    label_opts=opts.LabelOpts(is_show=False),
    is_smooth=True,
    markpoint_opts=opts.MarkPointOpts(
        data=[opts.MarkPointItem(type_="max", name="最大值"),
              opts.MarkPointItem(type_="min", name="最小值")],
    ),
)

# 配置项设置
line.set_global_opts(
    title_opts=opts.TitleOpts(title="2023年行业平均工资与增长率"),
    tooltip_opts=opts.TooltipOpts(trigger="axis"),
    yaxis_opts=opts.AxisOpts(
        type_="value",
        name="行业平均工资",
        min_=min(industry_wages)*0.9,
        max_=max(industry_wages)*1.1,
        interval=20000,
        axistick_opts=opts.AxisTickOpts(is_show=True),
        splitline_opts=opts.SplitLineOpts(is_show=True),
    ),
    xaxis_opts=opts.AxisOpts(type_="category", name="行业"),
    legend_opts=opts.LegendOpts(is_show=True),
    toolbox_opts=opts.ToolboxOpts()
)

# JsCode 函数来自 pyecharts
# 添加增长率数据
line.extend_axis(
    yaxis=opts.AxisOpts(
        type_="value",
        name="行业工资增长率",
        min_=min(growth_rates)*0.9,
        max_=max(growth_rates)*1.1,
        interval=2,
        axislabel_opts=opts.LabelOpts(formatter="{value} %"),
        axistick_opts=opts.AxisTickOpts(is_show=True),
        splitline_opts=opts.SplitLineOpts(is_show=False),
    )
)
line.set_series_opts(
    markline_opts=opts.MarkLineOpts(
        label_opts=opts.LabelOpts(position="middle", formatter=JsCode("function (params) { return params.value+' %'; }")),
        data=[opts.MarkLineItem(y=min(growth_rates)*0.9, name="增长率最小值"),
              opts.MarkLineItem(y=max(growth_rates)*1.1, name="增长率最大值")]
    )
)

# 将 Y 轴的增长率数据与折线图关联
line.add_yaxis(
    series_name="行业工资增长率",
    yaxis_index=1,
    y_axis=growth_rates,
    label_opts=opts.LabelOpts(is_show=False),
    is_smooth=True
)

# 渲染图表到 HTML 文件
line.render("line_chart_industry_wages.html")
```
## 分析2:不同行业的工资增长率是否存在显著差异？
**涉及数据**：['行业分类', '行业工资增长率']
**解读**：不同行业的工资增长率存在显著差异，如金融业增长率最高为13.4%，水利、环境和公共设施管理业最低为0.6%。 
**可视化代码**：
```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 行业分类
categories = [
    "总体", "农、林、牧、渔业", "采矿业", "制造业",
    "电力、热力、燃气及水生产和供应业", "建筑业", "批发和零售业",
    "交通运输、仓储和邮政业", "住宿和餐饮业", "信息传输、软件和信息技术服务业",
    "金融业", "房地产业", "租赁和商务服务业", "科学研究和技术服务业",
    "水利、环境和公共设施管理业", "居民服务、修理和其他服务业", "教育",
    "卫生和社会工作", "文化、体育和娱乐业", "公共管理、社会保障和社会组织"
]

# 行业工资增长率
growth_rates = [5.8, 6.7, 11.1, 6.6, 8.0, 9.6, 7.8, 6.4, 7.6, 5.2, 13.4, 1.8, 2.6, 4.9, 0.6, 5.3, 3.0, 6.4, 5.1, -0.3]

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.NONE))
    .add_xaxis(categories)
    .add_yaxis("行业工资增长率", growth_rates, itemstyle_opts=opts.ItemStyleOpts(color=JsCode("""
        function(params) {
            var colorList = ['#5470C6', '#91CC75', '#EE6666', '#73C0DE', '#3BA272', '#FC8452', '#9A60B4', '#ea7ccc'];
            return colorList[params.dataIndex % colorList.length];
        }
    """)))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2023年不同行业的工资增长率"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        yaxis_opts=opts.AxisOpts(name="增长率（%）"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .render("industry_growth_rate_2023.html")
)
```
## 分析3:各行业的平均工资与城镇非私营单位就业人员的平均工资相比如何？
**涉及数据**：['行业分类', '城镇非私营单位就业人员年平均工资', '行业平均工资']
**解读**：各行业平均工资中，信息传输、软件和信息技术服务业、金融业、科学研究和技术服务业、卫生和社会工作等行业高于城镇非私营单位平均工资，其余行业低于。 
**可视化代码**：
```
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

# 数据集
year = "2023"
avg_wage_of_non_private_employees = 120698
industry_avg_wages = {
    "农、林、牧、渔业": 62952,
    "采矿业": 135025,
    "制造业": 103932,
    "电力、热力、燃气及水生产和供应业": 143594,
    "建筑业": 85804,
    "批发和零售业": 124362,
    "交通运输、仓储和邮政业": 122705,
    "住宿和餐饮业": 58094,
    "信息传输、软件和信息技术服务业": 231810,
    "金融业": 197663,
    "房地产业": 91932,
    "租赁和商务服务业": 109264,
    "科学研究和技术服务业": 171447,
    "水利、环境和公共设施管理业": 68656,
    "居民服务、修理和其他服务业": 68919,
    "教育": 124067,
    "卫生和社会工作": 143818,
    "文化、体育和娱乐业": 127334,
    "公共管理、社会保障和社会组织": 117108,
}

industries = list(industry_avg_wages.keys())
wages = list(industry_avg_wages.values())

# 生成可视化代码
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.NONE))
    .add_xaxis(list(industries))
    .add_yaxis("平均工资", list(wages))
    .add_yaxis("城镇非私营单位平均工资", [avg_wage_of_non_private_employees]*len(industries))
    .set_global_opts(
        title_opts=opts.TitleOpts(title=f"{year}年各行业平均工资对比图"),
    )
    .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
    )
)

# 渲染
bar.render("salary_compare.html")
```
在这段代码中，我们首先定义了数据集，包括年份、城镇非私营单位的平均工资以及各行业的平均工资。然后我们创建了一个bar对象，设置了一系列的选项（如主题、X轴和Y轴标签等）。最后，我们将图表渲染成一个HTML文件。
## 分析4:城镇非私营单位就业人员年平均工资的涨幅比率是否与经济发展水平相关？
**涉及数据**：['年份', '涨幅比率']
**解读**：数据未包含经济发展水平指标，无法直接判断城镇非私营单位就业人员年平均工资涨幅比率与经济发展水平的关系。 
**可视化代码**：
```
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType

data = [
    ("农、林、牧、渔业", 62952, 6.7),
    ("采矿业", 135025, 11.1),
    ("制造业", 103932, 6.6),
    ("电力、热力、燃气及水生产和供应业", 143594, 8.0),
    ("建筑业", 85804, 9.6),
    ("批发和零售业", 124362, 7.8),
    ("交通运输、仓储和邮政业", 122705, 6.4),
    ("住宿和餐饮业", 58094, 7.6),
    ("信息传输、软件和信息技术服务业", 231810, 5.2),
    ("金融业", 197663, 13.4),
    ("房地产业", 91932, 1.8),
    ("租赁和商务服务业", 109264, 2.6),
    ("科学研究和技术服务业", 171447, 4.9),
    ("水利、环境和公共设施管理业", 68656, 0.6),
    ("居民服务、修理和其他服务业", 68919, 5.3),
    ("教育", 124067, 3.0),
    ("卫生和社会工作", 143818, 6.4),
    ("文化、体育和娱乐业", 127334, 5.1),
    ("公共管理、社会保障和社会组织", 117108, -0.3),
]

c = (
    Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([d[0] for d in data])
    .add_yaxis("城镇非私营单位就业人员年平均工资", [(d[1], d[2]) for d in data])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="城镇非私营单位就业人员年平均工资涨幅比率及行业平均工资"),
        xaxis_opts=opts.AxisOpts(name="行业"),
        yaxis_opts=opts.AxisOpts(name="涨幅比率及工资", axislabel_opts=opts.LabelOpts(formatter="{value} 元")),
        visualmap_opts=opts.VisualMapOpts(type_="size", max_=200000, min_=50000),
        tooltip_opts=opts.TooltipOpts(formatter="{b}<br/>工资：{c[0]} 元 <br/>涨幅比率：{c[1]} %"),
    )
)

c.render("scatter_analysis.html")
```
这段代码将生成一个可视化图表，x轴是行业，y轴是涨幅比率及城镇非私营单位就业人员年平均工资。生成的html文件名为"scatter_analysis.html"。图标的数据点大小基于工资值，显示了各行业的年平均工资以及其涨幅比率。
## 分析5:哪些行业在过去几年中表现出较高的工资增长率？
**涉及数据**：['年份', '行业分类', '行业工资增长率']
**解读**：2023年，金融业、采矿业和建筑业的工资增长率分别为13.4%，11.1%和9.6%，表现出较高的工资增长率。 
**可视化代码**：
```
from pyecharts import options as opts
from pyecharts.charts import Bar

# 数据集（此处简化为Python数据，实际使用时可能需要从文件或数据库中读取）
data_list = [
    ('总体', 120698, 5.8),
    ('农、林、牧、渔业', 62952, 6.7),
    ('采矿业', 135025, 11.1),
    ('制造业', 103932, 6.6),
    ('电力、热力、燃气及水生产和供应业', 143594, 8.0),
    ('建筑业', 85804, 9.6),
    ('批发和零售业', 124362, 7.8),
    ('交通运输、仓储和邮政业', 122705, 6.4),
    ('住宿和餐饮业', 58094, 7.6),
    ('信息传输、软件和信息技术服务业', 231810, 5.2),
    ('金融业', 197663, 13.4),
    ('房地产业', 91932, 1.8),
    ('租赁和商务服务业', 109264, 2.6),
    ('科学研究和技术服务业', 171447, 4.9),
    ('水利、环境和公共设施管理业', 68656, 0.6),
    ('居民服务、修理和其他服务业', 68919, 5.3),
    ('教育', 124067, 3.0),
    ('卫生和社会工作', 143818, 6.4),
    ('文化、体育和娱乐业', 127334, 5.1),
    ('公共管理、社会保障和社会组织', 117108, -0.3)
]

x_data = [item[0] for item in data_list]
y_data = [item[2] for item in data_list]

# 创建折线图对象
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("年工资增长率", y_data)
    .set_global_opts(title_opts=opts.TitleOpts(title="各行业工资增长率"),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
                     yaxis_opts=opts.AxisOpts(name="%"))
     # 自动在最高值处标记
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(type_="max", name="最大值")]
        )    
    )
)

# 生成图表
bar.render("bar.html")
```
在这段Pyecharts代码中，先定义了数据集，然后创建一个柱状图对象，并设置了x轴、y轴的数据，接着设置了整个图的全局样式及关键点的标记点，并最后生成了图表。注意因为行业名称较长，因此对x轴的标签进行了旋转处理。
## 分析6:工资增长率与行业平均工资是否存在相关性？
**涉及数据**：['行业工资增长率', '行业平均工资']
**解读**：金融业工资增长率最高且平均工资较高表明高收入行业增长迅速需关注收入差距 
**可视化代码**：
```
from pyecharts import options as opts
from pyecharts.charts import Scatter
import pandas as pd

# 数据集准备
data = {
    "行业分类": [
        "总体", "农、林、牧、渔业", "采矿业", "制造业", "电力、热力、燃气及水生产和供应业",
        "建筑业", "批发和零售业", "交通运输、仓储和邮政业", "住宿和餐饮业",
        "信息传输、软件和信息技术服务业", "金融业", "房地产业", "租赁和商务服务业",
        "科学研究和技术服务业", "水利、环境和公共设施管理业", "居民服务、修理和其他服务业",
        "教育", "卫生和社会工作", "文化、体育和娱乐业", "公共管理、社会保障和社会组织"
    ],
    "行业平均工资": [
        120698, 62952, 135025, 103932, 143594, 85804, 124362, 122705, 58094,
        231810, 197663, 91932, 109264, 171447, 68656, 68919, 124067, 143818,
        127334, 117108
    ],
    "行业工资增长率": [
        5.8, 6.7, 11.1, 6.6, 8.0, 9.6, 7.8, 6.4, 7.6, 5.2, 13.4, 1.8, 2.6, 4.9,
        0.6, 5.3, 3.0, 6.4, 5.1, -0.3
    ]
}
df = pd.DataFrame(data)

# 创建散点图
scatter = (
    Scatter()
    .add_xaxis(df['行业平均工资'].tolist())
    .add_yaxis("行业工资增长率", df['行业工资增长率'].tolist(), label_opts=opts.LabelOpts(formatter="{b}"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="行业平均工资与工资增长率相关性分析"),
        xaxis_opts=opts.AxisOpts(type_="value", name="行业平均工资"),
        yaxis_opts=opts.AxisOpts(type_="value", name="行业工资增长率"),
        visualmap_opts=opts.VisualMapOpts(type_='size', max_=15, min_=5)
    )
)

scatter.render("industry_wage_growth_correlation.html")
```
# 以下是按照government_client风格生成的数据解读：
 报告标题：城市非私营就业人员工资水平及其增长趋势与行业分析报告

各位在座的同仁，今日我们来探讨一份2023年涵盖各个行业的城市非私营就业人员工资水平以及他们的工资增长趋势。而通过深入分析这份数据，我们希望为政策制定者提供关于如何提高公众就业满意度，参与公平财富分配以及制定策略促进经济发展的洞察。

首先，2023年非私营部门的平均工资涨幅比率为5.8%，这显示出我国非私营就业人员的工资呈稳步上升的趋势。这是一个积极的经济指标，体现了我国经济的稳定性以及良好的发展空间。同时，这也暗示了我们的政策制定者需要持续关注非私营部门的工资发展情况。

其次，我国各行业的工资增长率呈现出明显的差异。其中，金融业、采矿业和建筑业的工资增长率主导了整个榜单。特别是金融业，其工资增长率高达13.4%，属于高收入行业。在这其中，我们不仅看到各行业的发展机会，同时也要重视收入差距的问题。

但是，请注意！并非所有行业都在同样的增长轨道上，如水利、环境和公共设施管理业的工资增长率是最低的，仅为0.6%。这就需要政府的关注，我们需要寻找原因，制定和执行更有效的政策，鼓励这些行业的发展，和解决他们的工资问题。

还有我们需要关注的是，与城镇非私营单位的平均工资相比，信息传输、软件和信息技术服务业、金融业、科学研究和技术服务业、卫生和社会工作等行业的工资水平较高；而其他行业如农林牧渔、制造业、建筑业等的工资水平则低于平均水平。

各位，我们能从这些数据中看出，虽然我们在提升就业人员工资方面取得了一定的成果，但也需要关注和解决行业之间的薪资差异。协调好这些问题，对于我们实现社会公平、平稳发展，实现国家的长远发展至关重要。

这便是我们现阶段能从这份数据中分析得出的情况。当然，如何解决这些问题，需要我们更深层次的研究，更精准的政策，以及我们大家的共同努力。感谢各位的关注与倾听。
        