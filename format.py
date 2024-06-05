class Format:
    def md(self,data,items,codelist,new,tone,url):
        '''

        :param items:
        :param codelist:
        :param new:
        :param tone:
        :return:
        '''
        st_items=items.strip()

        md_data=f"""# 整理后的原始数据是：\n{data}\n """
        md_text = f"""# 该数据包含的主要维度：\n{st_items}\n"""

        md_anaa = "# 以下是关于数据的分析与可视化：\n"

        # cc=eval(codelist)
        cc=codelist

        for i in cc:

            discription = i

            index = discription['index']
            question = discription['question']
            attribute = discription['attributes']
            analysis = discription['analysis']
            code = discription['code']

            md_ana = f"""## 分析{index}:{question}\n**涉及数据**：{attribute}\n**解读**：{analysis} \n**可视化代码**：\n{code}\n"""

            md_anaa = ''.join([md_anaa, md_ana])

        nn_new=new.strip()

        md_new=f"""# 以下是按照{tone}风格生成的数据解读：\n {nn_new}\n
        """

        md_pc=f"# 以下是AI根据稿件主题生成的插图\n{url}"

        allmd = md_data+md_text + md_anaa+md_new+md_pc
        # allmd = md_data+md_text + md_anaa+md_new

        # allmd = f'''# 该数据包含的主要维度：\n{items}\n# 数据解读与分析：\n
        # {items}\n#'''

        with open(f'./temp/md文件.md', 'w', encoding='utf-8') as file:
            file.write(allmd)

        print("完整数据报告已生成完毕")

        pass
