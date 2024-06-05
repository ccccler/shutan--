
class Repair:

    from config import config_client
    from chartstyle import Chart
    from character import Character
    from shutan import Shutan
    def visre(self,i,input,path):

        with open(f'{path}', 'r', encoding='utf-8') as file:
            viz = file.read()

        self.vlist = eval(viz)

        client=self.config_client

        raw_vis=self.vlist[i]

        num=raw_vis['index']

        question=raw_vis['question']

        rawcode=raw_vis['code']

        system_prompt = f'''
                     你是一位熟练编写Pyecharts v2.0可视化代码的助手。你熟悉Pyecharts v2.0版本的各种配置项，能够根据要求对pyecharts代码进行修改。\
                     我将给你提供一个已经写好的Pyecharts v2.0的代码，请你根据我的修改要求，对其进行修改，并反馈给我修改好的新的pyecharts v2.0代码。\
                     注意，在修改时，你只需要修改我要求你的地方，其他的地方一律保持不变，原来的代码是什么样就是什么样。\
                     注意，你必须返回一个以import语句开头的包含在BACKTICKS符号```中的完整PYTHON程序。不要输出任何与代码无关的其他内容。'''

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"原始代码是{rawcode}，它所描述的修改要求是{input}。请你保持其他代码部分不变，只修改\
                我要求的部分。修改后的代码是"}
            ],
            # temperature=0
        )

        output = completion.choices[0].message.content


        md_ana = f"""## 分析{num}:{question}\n原可视化代码是:\n{rawcode}\n修改后的可视化代码是:\n{output}"""

        with open(f'./temp2/代码修改档案.md', 'w', encoding='utf-8') as file:
            file.write(md_ana)

        print("代码修改完毕，请在修改档案中查看")

    def anavisre(self,data_path,input_role,question,background):

        client=self.config_client

        with open(f'{data_path}', 'r', encoding='utf-8') as file:
            data = file.read()

        a = self.Character()
        dis = a.get_prompt(input_role)

        # 以下是生成分析结果的响应
        system_prompt = f'''你是一个数据分析机器人。能够按照特定视角，根据我提供给你的问题对数据进行分析。你的视角是{input_role}，
                        该视角的特点是{dis}。数据是{data}。该数据的背景是{background}。
                     '''

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"我需要你以{input_role}的视角，读取数据，帮我回答{question}问题。你的回答是:"}
            ],
            temperature=0.5
        )
        # 获得问题回答
        ana = completion.choices[0].message.content

        print(f"回答已完成，回答是：{ana}")

        # 以下是生成新图表的响应
        system_prompt1 = "你是一位熟练编写Pyecharts v2.0可视化代码的助手。你可以根据数据集本身、要求解决的问题，\
                    自动给我推荐一个适合该数据的可视化图表类型。推荐的图表类型必须从[bar],[bar_stack],[bar_x],[box_plot],[calender],[funnel],\
                    [k_line],[line],[line_area],[pie],[scatter]这11种当中选一个，不允许推荐在这个11个之外的任何图表类型。选择好之后，请你直接给我反馈该图表的名称,\
                    不允许反馈任何其他不相关的内容。# 请一定记住只能从这几个里面选。"

        ep_data = '''日期	价格
                            2023年11月05日	21.1400
                            2023年10月29日	21.3200
                            2023年10月22日	21.6800
                            2023年10月15日	21.7600'''

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
        # 获得推荐图表类型
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
                 "content": f'''数据集是{data}，你的可视化需要解决的问题是{question}，请你选用{re_chart}图表类型，使用LIGHT主题，根据以上信息生成它的可视化代码。你生成的代码是'''}
            ],
            temperature=0
        )

        # 获得问题的可视化代码
        output = completion.choices[0].message.content

        print(f"新问题已可视化完成,推荐类型为{re_chart}")

        # 开始整合

        md_ana = f"""## 问题{question}\n分析结论是：\n{ana}\n可视化代码是:\n{output}"""

        with open('./temp2/添加分析档案.md', 'w', encoding='utf-8') as file:
            file.write(md_ana)

        print("新问题回答完毕，请在[添加分析档案.md]中查看")

    def newsre(self,background,role,news_path,input,data,url):

        client=self.config_client

        with open(f'{news_path}', 'r', encoding='utf-8') as file:
            news = file.read()

        # with open(f'{ana_path}', 'r', encoding='utf-8') as file:
        #     ana = file.read()

        # with open(f'{url_path}', 'r', encoding='utf-8') as file:
        #     url = file.read()

        system_prompt=f'''你是一个新闻审稿人。请你以{role}的视角和身份，根据要求，对一篇文字进行修改。该文字的背景是{background},
                        所讲述的数据是{data}。在修改完成后，请你返回给我生成好的文稿。'''

        completion=client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"原新闻是{news},修改要求是{input}，你修改好的新闻稿是："
                 },
],
            temperature=1
        )

        # 获得问题的可视化代码
        gcnew = completion.choices[0].message.content
        print("新稿子修改完毕")

        md_news = f"""修改要求是：\n{input}\n修改完成的稿子是:\n{gcnew}\nAI图片链接是\n{url}"""

        with open('./temp2/修改报告档案.md', 'w', encoding='utf-8') as file:
            file.write(md_news)

        print("报告修改完毕，请在[修改报告档案.md]中查看")


