class Shutan():
    """该类是产品的功能区块"""
    # -*- coding: utf-8 -*-
    from config import config_client
    from chartstyle import Chart
    from character import Character
    from PIL import Image
    from io import BytesIO
    from openai import OpenAI
    import requests

    def item_extraction(self, input):
        '''
        该函数用来提取非结构和结构化数据中，可能涉及到的数据维度。
        :param input: 原始数据
        :return: 一个dict格式的数据维度字典。包括维度名称、维度的数据类型、以及对该维度的描述
        '''

        client = self.config_client
        system_prompt = '''你是一个数据提取机器人。你的作用是从一段文本当中提取出可能存在的数据的多个共同属性,以方便将这段文本转化成一份结构化的数据。
                    你所要输出的是一个个若干个属性名称、各个属性所适合的数据类型（字符、数值、类别）以及关于该属性的描述，并以dict的格式反馈给我。
                    dict的格式是：  {"维度n": {
                    "name": "",
                    "type": "",
                    "discription":""
                        }}
                    请你只反馈给我属性的dict格式信息，不要返回任何其他不相关的内容。注意，你只需要返回形式为dict的字符串，而无需返回任何其他的内容。
                    不要放在类似```的BACKTICKS里。'''

        user_prompt = '''根据最新的销售数据显示，比亚迪以133,317辆的销量稳居榜首，占据了整体市场的10.29%份额。紧随其后的是长安汽车，
        其销量达到90,067辆，占据了6.95%的市场份额。而第三名则被上汽大众所占据，其销量为78,000辆，占据了整体市场的6.02%份额。
        一汽-大众以70,004辆的销量位列第四，占据了5.41%的市场份额。吉利汽车以67,479辆的销量排名第五，占据了5.21%的市场份额。'''

        ai_prompt = '''{
          "维度1": {
            "name": "排名",
            "type": "int",
            "discription":"该属性描述了数据中各个汽车品牌的销售排名"
          },
          "维度2": {
            "name": "品牌名称",
            "type": "str",
            "discription":"该属性描述了数据中各个汽车品牌的名称"
          },
          "维度3": {
            "name": "销量",
            "type": "int",
            "discription":"该属性描述了数据中各个汽车品牌的销量"
          },
          "维度4": {
            "name": "占销量份额",
            "type": "int",
            "discription":"该属性描述了数据中各个汽车品牌销量所占的销售份额"
          },
        }'''

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": ai_prompt},
                {"role": "user", "content": input},
            ],
            temperature=0
        )

        items = completion.choices[0].message.content

        titems = f"{items}\n"

        filename = "./temp/items_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(titems)
        print("item已保存")

        return items

    def data_extraction(self, items, raw_data):
        '''
        该函数根据前一个函数提取出来的数据属性，对原始数据进行结构化提取。最终将原始数据转化为一个dataframe格式的结构化数据
        :param items: 数据维度
        :param raw_data:原始数据
        :return: 一个dataframe格式的结构化数据
        '''

        client = self.config_client

        system_prompt = '''你是一个数据提取机器人，擅长将非结构化数据转化为dataframe格式的结构化数据。我将给你提供一段非结构化数据data，
        以及该数据中存在的各个数据属性item。
        请你根据item，将data当中对应的数据一个不落的归纳为一份完整的结构化的dataframe格式数据。
        请注意，你只被允许输出一份完整的dataframe格式的数据。我将给你提供一个例子。
        请你严格按照这个例子的形式，返回一种不带BACKTICKS```符号的str格式的数据文本，不允许输出任何以与dataframe格式数据无关的内容。'''
        user_prompt = '''data："根据最新的销售数据显示，比亚迪以133,317辆的销量稳居榜首，占据了整体市场的10.29%份额。
        紧随其后的是长安汽车，其销量达到90,067辆，占据了6.95%的市场份额。而第三名则被上汽大众所占据，其销量为78,000辆，
        占据了整体市场的6.02%份额。一汽-大众以70,004辆的销量位列第四，占据了5.41%的市场份额。吉利汽车以67,479辆的销量排名第五，
        占据了5.21%的市场份额。"
    item:"{
      "attribute1": {
        "name": "排名",
        "type": "int"
        "discription":"该属性描述了数据中各个汽车品牌的销售排名"
      },
      "attribute2": {
        "name": "厂商",
        "type": "str"
        "discription":"该属性描述了数据中各个汽车品牌的名称"
      },
      "attribute3": {
        "name": "销量",
        "type": "int"
        "discription":"该属性描述了数据中各个汽车品牌的销量"
      }"
      '''
        ai_prompt = '''排名	厂商	销量	
    1	比亚迪	133317	
    2	长安汽车	90067	
    3	上汽大众	78000	
    4	一汽-大众	70004	
    5	吉利汽车	67479	'''

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": ai_prompt},
                {"role": "user", "content": "data:" + raw_data + "items:" + items},
            ],
            temperature=0
        )

        format_data = completion.choices[0].message.content

        tformat = f"{format_data}\n"

        filename = "./temp/data_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(tformat)
        print("data已保存")

        return format_data

    def goal_explore(self, item, input_role="general", background="这是一份数据"):
        '''
        该函数根据之前提取好的数据维度，探索这些数据维度之间可能存在什么关系。并且可以自己设定能够提取多少关系
        :param item: 数据维度
        :param input_role: 以什么身份和视角探索该数据，默认为通用
        :param background: 该数据的背景是什么
        :return: 一个dict格式的包含问题的文本
        '''
        client = self.config_client

        system_prompt = '''你是一个数据分析Agent，可以分析一个数据集中不同维度数据之间的关系。我将给你提供一个数据集的具体维度数据介绍。\
    该介绍是dict格式。请你根据该维度介绍，以特定的身份视角先推断该数据的数据维度之间可能会存在哪些关联，并反馈n个可能存在关联的维度，以dict格式。
    反馈的内容包括索引、对可能出现的数据关系的探讨，以及涉及到的数据维度。反馈的格式是：
    {
        "探索1": {
        "index":1
        "question": "不同产品之间的销量分布是什么",
        "attributes": ["产品名称","销量"]},
      "探索2"：{
        "index":2
        "question": "该产品的销量怎样随着变化？",
        "attributes": ["日期","销量"]},
      ......
      }

    注意，你只需要返回形式为dict的字符串，而无需返回任何其他的内容。不要放在```这样的BACKTICKS里。'''

        a = self.Character()
        dis = a.get_prompt(input_role)
        # print(dis)

        prompt = [
            {"role": "system", "content": system_prompt},
            {"role": "user",
             "content": f'''该数据集的背景是{background},你需要用{input_role}的身份来进行分析，该身份的特点是{dis}。你所基于的维度描述是{item}'''}
            # {"role": "user", "content":f'''你需要返回的探索数量是{n}个，你所基于的维度描述是{item}'''}
        ]

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=prompt,
            temperature=0.5
        )

        goals = completion.choices[0].message.content

        tgoals = f"{goals}\n"

        filename = "./temp/goals_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(tgoals)
        print("goal已保存")

        return goals

    def goal_analysis(self, goals, data, input_role="general", background="这是一份数据"):
        '''
        该函数用来分析上一步探索出来的问题
        :param goals: 上一步的问题列表
        :param data: dataframe格式数据
        :param input_role: 以何种视角分析解读数据
        :param background: 该数据的背景
        :return: 一个dict格式的包含分析结论的内容
        '''

        client = self.config_client

        # dictionary_data = json.loads(goals)

        goals = eval(goals)

        # print(dictionary_data)

        goals_list = []

        # 将每个探索项添加到列表中
        goals_list = [{k: v for k, v in sub_dict.items()} for sub_dict in goals.values()]

        # print(goals_list)

        analysis_list = []

        a = self.Character()
        dis = a.get_prompt(input_role)
        # print(dis)

        system_prompt = "你是一个数据分析Agent。能够根据给定的身份，以其视角对数据进行分析。我将给你一份数据，以及你要回答的问题，和涉及到的\
                      具体维度。反馈的格式只需要一串完整的字符串即可，不要其他任何符号。"

        # system_prompt = "你是一个数据分析大师。请你基于数据集里的数据，对我给你提供的问题以及涉及到的数据维度进行分析。注意\
        #                   分析结论不需要有任何换行符，只需要一串完整的字符串即可。"

        for i in goals_list:
            # print(i)
            singlee = i
            single = str(i)
            # print(single)

            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",
                     "content": f'''数据集是{data}，该数据集的背景是{background},你需要以{input_role}的视角来分析该数据，该视角的特点有{dis},\
                    你所需要探索的问题和涉及维度是{single}'''}
                ],
                temperature=0.5
            )

            output = completion.choices[0].message.content
            # print(output)

            analysis = {'analysis': output}

            singlee.update(analysis)

            # singleee=eval(singlee)
            # print(singlee)

            analysis_list.append(singlee)

        tanalysis = f"{analysis_list}\n"

        filename = "./temp/ana_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(tanalysis)
        print("anal已保存")

        return analysis_list

    def visualization_all(self, data, list, color="LIGHT", chart_input="你认为最合适的", ):
        '''
        该函数用来给上述分析结果生成可视化表
        :param data:dataframe格式数据
        :param list: goal explpre的集
        :param color: 可视化风格，默认为light
        :param chart_input: 图表类型，默认不用
        :return:一个包含可视化代码的集
        '''

        client = self.config_client

        code_list = []

        # alist = eval(list)

        alist = list

        for i in alist:
            # print(i)

            discription = i
            # print(discription)

            question = discription['question']

            num = discription['index']

            system_prompt1 = "你是一位熟练编写Pyecharts v2.0可视化代码的助手。你可以根据数据集本身、要求解决的问题，\
            自动给我推荐一个适合该数据的可视化图表类型。推荐的图表类型必须从[bar],[bar_stack],[bar_x],[box_plot],[calender],[funnel],\
            [k_line],[line],[line_area],[pie],[scatter]这11种当中选一个，不允许推荐在这个11个之外的任何图表类型。选择好之后，请你直接给我反馈该图表的名称,\
            不允许反馈任何其他不相关的内容。# 请一定记住只能从这几个里面选。"

            ep_data = '''日期	价格
                    2023年11月05日	21.1400
                    2023年10月29日	21.3200
                    2023年10月22日	21.6800
                    2023年10月15日	21.7600
                    2023年10月08日	22.0900
                    2023年10月01日	22.3800
                    2023年09月24日	22.5300
                    2023年09月10日	22.8700
                    2023年09月03日	23.0900'''

            ep_question = "价格和日期的变动关系如何？"

            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt1},
                    {"role": "user", "content": f"数据集是{ep_data}，你的可视化需要解决的问题是{ep_question}"},
                    {"role": "assistant", "content": "line"},
                    {"role": "user", "content": f'''数据集是{data}，你的可视化需要解决的问题是{question}'''}
                ],
            )

            re_chart = completion.choices[0].message.content

            c = self.Chart()

            d = getattr(c, re_chart)

            f = d.ex_code
            # print(f)

            system_prompt = f'''
             你是一位熟练编写Pyecharts v2.0可视化代码的助手。你可以根据数据集、要求解决的问题、选用的图表类型，\
             对相应数据进行可视化代码生成。你熟悉Pyecharts v2.0版本的各种配置项，能够选用各种配置项来对可视化图表进行装饰，例如标记线、最大值最小值标记等。\
             注意，生成的图表需要包含所有有效的信息，请勿因为图片尺寸遗漏或者隐藏某些信息，你可以通过调整字体大小来解决这一问题。注意，有些数据集里可能包含中文字符，请你在可视化时考虑使用合适的方式让中文字符也能够成功展现。\
             注意，你需要使用的是Pyecharts v2.0这个可视化图表中的{re_chart}类图表。你必须返回一个以import语句开头的包含在BACKTICKS符号```中的完整PYTHON程序。\
             不要输出任何与代码无关的其他内容。一定记住以```+代码的格式返回，不用返回任何其他说明文字。我将给你提供一个例子'''

            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"这是{re_chart}类型图表的示例代码:{f}"},
                    {"role": "user",
                     "content": f'''数据集是{data}，你的可视化需要解决的问题是{question}，请你选用{re_chart}图表类型，使用{color}主题，根据以上信息生成它的可视化代码。你生成的代码是'''}
                ],
                temperature=0
            )

            output = completion.choices[0].message.content

            print(f"第{num}个问题已可视化完成,问题是{question},推荐类型为{re_chart}")

            code = {'code': output}

            discription.update(code)

            code_list.append(discription)

        tcodelist = f"{code_list}\n"

        filename = "./temp/vis_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(tcodelist)
        print("vis已保存")

        return code_list

    def newsgenerate(self, data, goalslist, background: str, input_role="general"):
        '''
        根据分析结论，整合形成的一篇数据报告
        :param data:dataframe格式数据
        :param goalslist:分析结论集
        :param background: 数据背景
        :param input_role:以何种身份视角分析
        :return:一篇包含对该数据解读的数据报告
        '''

        client = self.config_client

        a = self.Character()
        dis = a.get_prompt(input_role)

        QAlist = []

        # ggl=eval(goalslist)
        ggl = goalslist

        for i in ggl:
            temp = i

            num = temp['index']
            numt = str(num)
            question = temp['question']
            analysis = temp['analysis']

            qa = {'问题' + numt: question, '解读' + numt: analysis}

            QAlist.append(qa)

        stringQA = ', '.join([', '.join([f"{key}: {value}" for key, value in d.items()]) for d in QAlist])

        system_prompt = f"你是一个数据解读者，能够根据数据内容和对该数据已有的一些分析和背景，形成一篇完整的有关这份数据的解读新闻。在形成报告时，\
                      你需要对该数据进行主题介绍、关系分析等等，并且确保在数据的使用上必须准确无误。你需要把所有已有的数据分析全部囊括进去，\
                      不允许有遗漏，当然你也可也添加一些你的其他发现，但前提是必须保证数据使用没有错误。在讲述时，你需要模仿{input_role}的语言风格，\
                      它的语言风格是{dis}，让新闻变得生动有趣。"

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",
                 "content": f'''数据集是{data}，关于该数据的背景是{background},该数据已有的一些解读是{stringQA},你需要\
                模仿的语气是{input_role}'''}
            ],
            temperature=1
        )

        output = completion.choices[0].message.content

        toutput = f"{output}\n"

        filename = f"./temp/news_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(toutput)
        print("news已保存")

        return output

    def pcgenerate(self, data, background):
        '''
        该函数用来生成与上述报告相关的插画
        :param data:  原始数据
        :param background: 该数据背景
        :return: 一个AI插画图
        '''
        ## 提取实体

        client = self.config_client

        system_prompt = '''请你从以下数据集中抽取一些可以用来生成图像的要素。我将给你提供数据集。请你给我反馈最多5个要素，并且直接以要素名称的形式
        反馈，类似“黑金、木头、月亮”这样，不要附加其他内容。'''

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f'''数据集是{data}'''}
            ],
            temperature=0.5
        )

        output = completion.choices[0].message.content

        # print(output)

        use_prompt = '''你是一个插画大师。我需要为一段新闻生成一张适合其主题的配图，我将给你提供涉及到的一些实体,请你给这些实体生成一张插画。
        整体图像应该尽可能简洁，并且采用concept的风格。请注意，在生成的插画里不要包含任何字符或者数字信息，只需要描绘一些符合主题的图像即可。'''

        prompt = f"{use_prompt},涉及到的实体是：{output},该数据的背景是{background}。注意，生成的插画里不要带有任何文字。"

        image = self.Image

        ss = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            style="vivid",
            size="1024x1024"
        )

        # print(ss)

        url = ss.data[0].url

        filename = "./temp/url_save"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(url)
        print("插图url已保存")

        # 打印响应结果
        # print(url)

        # response = requests.get(url)
        # output_path = './temp/output_image.png'

        # # 检查请求是否成功
        # if response.status_code == 200:
        #     # 使用BytesIO将内容转换为图像
        #     webp_image = Image.open(BytesIO(response.content))
        #
        #     # 保存为PNG格式的图片
        #     webp_image.save(output_path, 'PNG')
        #
        #     print(f"转换完成，图片已保存到: {output_path}")
        # else:
        #     print(f"无法获取WebP图片。状态码: {response.status_code}")

        # return output_path

        return url

