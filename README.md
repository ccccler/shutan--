# shutan--
一个以LIDA架构为基础的数据可视化与分析AIGC系统

# 使用方法
1.首先，包clone或下载到本地

2.在文件夹中创建一个名字叫temp的文件夹。
![image](https://github.com/ccccler/shutan--/assets/127079609/ba1e03c5-b121-4986-b93f-f796c923db2d)


3.安装包：
在terminal内，运行
```
pip install -r requirements.txt
```

5.在config.py文件中，更换自己API的base_url和api

4.在main.py文件中，实例化Run，调用内部的y函数，按照案例替换数据即可。最终生成的结果是一个Markdown文件，包括转化过的数据、数据描述、数据分析和可视化、以及数据报告
```
    input_data=''' '''

    background=""

    # 此处身份从character当中的模板选择
    shenfen="government_client"

    # 此处style从 LIGHT/DARK/CHALK/ESSOS/INFOGRAPHIC/MACARONS/ROMA/ROMANTIC/SHINE/WALDEN/WONDERLAND 中选择
    style="LIGHT"

    run_instance = Run()

    run_instance.y(input_data,background,shenfen,style,None)
```

5.如果想替换自己的身份或视角，在character.py中把身份的名称和描述按照上述格式加在下方，即可在main中调用
```
    def __init__(self):
        self.prompts = {
            "general": "一个善于分析数据的大师",
            "statistician": "一个统计学家。善于从数据当中洞察其中的深层次关系，严谨认真。",
            "journalist": "一个新闻记者。善于从新闻报道的角度来分析数据，懂得读者所关注的内容。",
            "government_client": "一个政府官员。善于挖掘数据当中对政府治理有价值的部分，从政府治理的角度分析数据。",
            "internet_celebrity": "一个社交网络红人。善于利用流行语言对数据进行解读和分析，并探索其中有价值的部分。",
            "xxxx":"xxxxxxx"
    }
```

6.如果想修改图表要求，实例化Repair类，调用里面的visre函数。输入修改要求，从缓存文件夹中读取旧表格，序号是说明要修改第几个图
```
    r=Repair()

    repair_input="请使用ESSOS主题，替换原来的主题。并用Line图对其进行表示。"

    path="./temp/vis_save"

    r.visre(1,repair_input,path)
```

7. 如果想新增分析和可视化，读取缓存文件夹中的原始数据，调用Repar类里面的anavisre函数。输入身份、新问题和数据背景
```
    question="行业平均工资排行前5的行业有哪些？他们普遍有什么特征？"

    data_path="./temp/data_save"

    r.anavisre(data_path,shenfen,question,background)
```

9. 如果想修改最终报告，读取缓存文件夹中的原始报告，结构化的数据，原始AI图片的URL。调用Repair类里的newsre函数，输入各参数
```
    with open('./temp2/url_save', 'r', encoding='utf-8') as file:
        url = file.read()

    new_path="./temp2/news_save"

    new_input="请你把这段文字修改成新闻稿形式的，不要现在这样发言稿类型的。以新闻稿的形式来总结"

    r.newsre(background,shenfen,new_path,new_input,data,url)
```
