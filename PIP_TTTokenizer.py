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
        # 加载 spaCy 的语言模型
        self.nlp = spacy.load("en_core_web_sm")

    def process_prompt(self, **kwargs):
        prompt = kwargs.get("文本", "")
        print(f"Processing prompt: {prompt}")
        
        # 替换指定的符号为英文逗号 ","
        for symbol in [",", ".", "，", "。"]:
            prompt = prompt.replace(symbol, ",")
        
        # 去除多余空格
        prompt = ' '.join(prompt.strip().split())
        
        # 使用 spaCy 处理输入的 prompt
        doc = self.nlp(prompt)
        
        # 计算 token 数量，忽略标点符号
        token_count = str(sum(1 for token in doc if not token.is_punct))
        
        # 提取自然语言描述并进行后处理
        # 按逗号分割 prompt
        phrases = prompt.split(',')
        long_phrases = []
        for phrase in phrases:
            words = phrase.strip().split()
            if len(words) > 2:
                long_phrases.append(phrase.strip())
        
        # 重新合并长短语作为自然语言描述
        natural_language_description = ', '.join(long_phrases)
        
        # 提取名词短语，并避免重复
        noun_phrases = set()
        noun_phrases_lower = set()
        for chunk in doc.noun_chunks:
            phrase = chunk.text.strip()
            phrase_lower = phrase.lower()
            # 排除无意义的短语
            if phrase_lower not in ['this image', 'that image', 'these images', 'those images']:
                noun_phrases.add(phrase)
                noun_phrases_lower.add(phrase_lower)
    
        # 记录已包含在短语中的词
        words_in_phrases = set()
        for phrase in noun_phrases:
            for word in phrase.lower().split():
                words_in_phrases.add(word)
        
        # 添加形容词 + 名词的组合，避免拆分已存在的短语
        for token in doc:
            word_lower = token.text.lower()
            if word_lower in words_in_phrases:
                continue  # 如果词已经在短语中，跳过
            if token.pos_ == 'ADJ' and token.dep_ == 'amod' and token.head.pos_ == 'NOUN':
                combined_phrase = f"{token.text} {token.head.text}"
                combined_phrase_lower = combined_phrase.lower()
                if combined_phrase_lower not in noun_phrases_lower:
                    noun_phrases.add(combined_phrase)
                    noun_phrases_lower.add(combined_phrase_lower)
                words_in_phrases.update([token.text.lower(), token.head.text.lower()])
            elif token.pos_ in ['NOUN', 'ADJ'] and word_lower not in ['this', 'that', 'these', 'those']:
                if word_lower not in words_in_phrases:
                    noun_phrases.add(token.text)
                    words_in_phrases.add(word_lower)
    
        # 移除被包含在其他短语中的词或短语
        final_phrases = set(noun_phrases)
        for phrase in noun_phrases:
            for other_phrase in noun_phrases:
                if phrase != other_phrase and phrase.lower() in other_phrase.lower():
                    if phrase in final_phrases:
                        final_phrases.remove(phrase)
                    break
    
        # 合并短语，并用逗号分隔
        clip_keywords = ", ".join(final_phrases)
        
        return token_count, natural_language_description, clip_keywords

# 定义节点类映射
NODE_CLASS_MAPPINGS = {
    "PIP_TTToken": PIP_TTToken
}

# 定义节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "PIP_TTToken": "PIP 分词器"
}
