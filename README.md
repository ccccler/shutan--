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


