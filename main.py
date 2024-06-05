# -*- coding: utf-8 -*-
from repair import Repair
from format import Format
from shutan import Shutan

class Run(Shutan,Format):

    '''该类用来整合运行所有过程，并将所有内容保存到一个md文件中'''

    def y(self,input_data,background,input_role,color,input_chart):

        items=self.item_extraction(input_data)
        data=self.data_extraction(items,input_data)
        goals=self.goal_explore(items,input_role,background)
        alis=self.goal_analysis(goals,data,input_role,background)
        viz=self.visualization_all(data,alis,color,input_chart)
        news=self.newsgenerate(data,alis,background,input_role)
        pc=self.pcgenerate(data,background)
        print("全部流程运行完毕")
        mdname="md文件"
        self.md(data,items,viz,news,input_role,pc)
        print("md文件已保存完成")

if __name__ == "__main__":

    # 以下用来正常运行

    input_data='''2023年，城镇非私营单位的就业人员年平均工资为120698元，比2022年的114029元增长了5.8%。其中，农、林、牧、渔业的平均工资为62952元，增长了6.7%；采矿业达到135025元，增长11.1%；制造业为103932元，增长6.6%。电力、热力、燃气及水生产和供应业的平均工资为143594元，增长8.0%；建筑业为85804元，增长9.6%；批发和零售业为124362元，增长7.8%；交通运输、仓储和邮政业为122705元，增长6.4%。住宿和餐饮业的平均工资为58094元，增长7.6%；信息传输、软件和信息技术服务业为231810元，增长5.2%；金融业为197663元，增长13.4%；房地产业为91932元，增长1.8%。租赁和商务服务业的平均工资为109264元，增长2.6%；科学研究和技术服务业为171447元，增长4.9%；水利、环境和公共设施管理业为68656元，增长0.6%；居民服务、修理和其他服务业为68919元，增长5.3%。教育行业的平均工资为124067元，增长3.0%；卫生和社会工作为143818元，增长6.4%；文化、体育和娱乐业为127334元，增长5.1%；而公共管理、社会保障和社会组织的平均工资为117108元，比2022年的117440元下降了0.3%。 '''

    background="2023年中国就业相关数据"

    shenfen="government_client"

    style="LIGHT"

    run_instance = Run()

    run_instance.y(input_data,background,shenfen,style,None)


    # help(s)

    ## 以下用来从缓存调用

    # with open('./temp/items_save', 'r', encoding='utf-8') as file:
    #     items = file.read()
    with open('./temp2/data_save', 'r', encoding='utf-8') as file:
        data = file.read()
    #

    # with open('./temp/vis_save', 'r', encoding='utf-8') as file:
    #     viz = file.read()
    # with open('./temp/news_save', 'r', encoding='utf-8') as file:
    #     news = file.read()
    # f=Format()
    #
    # f.md(data,items,viz,news,shenfen)


    ## 以下用来修改图表

    r=Repair()

    # repair_input="请使用ESSOS主题，替换原来的主题。并用Line图对其进行表示。"
    #
    # path="./temp2/vis_save"
    #
    # r.visre(1,repair_input,path)

    # question="行业平均工资排行前5的行业有哪些？他们普遍有什么特征？"

    # data_path="./temp2/data_save"
    #
    # r.anavisre(data_path,shenfen,question,background)
    with open('./temp2/url_save', 'r', encoding='utf-8') as file:
        url = file.read()

    new_path="./temp2/news_save"

    new_input="请你把这段文字修改成新闻稿形式的，不要现在这样发言稿类型的。以新闻稿的形式来总结"

    r.newsre(background,shenfen,new_path,new_input,data,url)




