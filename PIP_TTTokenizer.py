import spacy

class PIP_TTToken:
    # 定义输入和输出类型
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "文本": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("token数量", "自然语言", "CLIP短句")

    FUNCTION = "process_prompt"

    def __init__(self):
        print("Initializing PIP_TTToken...")
        # 加载spaCy的语言模型
        self.nlp = spacy.load("en_core_web_sm")

    def process_prompt(self, **kwargs):
        prompt = kwargs.get("文本", "")
        print(f"Processing prompt: {prompt}")
        # 使用spaCy处理输入的prompt
        doc = self.nlp(prompt)
        
        # 计算token数量，忽略标点符号
        token_count = str(sum(1 for token in doc if not token.is_punct))
        
        # 提取第一个完整的句子作为自然语言描述
        natural_language_description = ""
        for sent in doc.sents:
            if len(sent) > 1:
                natural_language_description = sent.text
                break
        
        # 提取短语（名词短语和单词）
        phrases = []
        for chunk in doc.noun_chunks:
            # 排除无意义的短语
            if chunk.text.lower() not in ['this image', 'that image', 'these images', 'those images']:
                phrases.append(chunk.text)
        
        # 提取单个名词和形容词短语，排除无意义的词
        for token in doc:
            if token.pos_ in ['NOUN', 'ADJ'] and token.text.lower() not in phrases and token.text.lower() not in ['this', 'that', 'these', 'those']:
                phrases.append(token.text)
        
        # 合并短语，并用逗号分隔
        clip_keywords = ", ".join(phrases)
        
        return token_count, natural_language_description, clip_keywords

# 定义节点类映射
NODE_CLASS_MAPPINGS = {
    "PIP_TTToken": PIP_TTToken
}

# 定义节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "PIP_TTToken": "PIP 分词器"
}