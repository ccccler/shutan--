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

4.在main.py文件中，实例化Run，调用内部的y函数，按照案例替换数据即可
```
    input_data=''' '''

    background=""

    shenfen="government_client"

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


