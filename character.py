class Character:
    def __init__(self):
        self.prompts = {
            "general": "一个善于分析数据的大师",
            "statistician": "一个统计学家。善于从数据当中洞察其中的深层次关系，严谨认真。",
            "journalist": "一个新闻记者。善于从新闻报道的角度来分析数据，懂得读者所关注的内容。",
            "government_client": "一个政府官员。善于挖掘数据当中对政府治理有价值的部分，从政府治理的角度分析数据。",
            "internet_celebrity": "一个社交网络红人。善于利用流行语言对数据进行解读和分析，并探索其中有价值的部分。"
        }

    def set_prompt(self, role, prompt):
        """设置指定身份的提示信息"""
        self.prompts[role] = prompt

    def get_prompt(self, role):
        """获取指定身份的提示信息"""
        return self.prompts.get(role, f"'{role}' prompt does not exist")