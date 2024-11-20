# PIP_TTToken 节点
## 概述
`PIP_TTToken` 是一个自然语言处理节点，使用 spaCy 库对输入文本进行分词和分析。此节点能够计算词元数量、提取自然语言描述，并生成 CLIP 关键词。
![微信截图_20241119194742](https://github.com/user-attachments/assets/77da3ea6-600a-4c63-ba25-a2b4256a3eb8)

## 功能
- **词元数量**：计算输入文本中的词元数量，忽略标点符号。
- **自然语言描述**：提取输入文本中的第一个完整句子作为自然语言描述。
- **CLIP 关键词**：从输入文本中提取名词短语和形容词短语，生成 CLIP 关键词。

## 输入
- **文本**：类型为 STRING，默认值为空字符串。输入的文本将被处理以提取信息。

## 输出
- **token数量**：类型为 STRING，表示输入文本中的词元数量。
- **自然语言**：类型为 STRING，表示提取的自然语言描述。
- **CLIP短句**：类型为 STRING，表示生成的 CLIP 关键词。

## 使用方法
1. 将 `PIP_TTToken` 节点添加到 ComfyUI 中。
2. 在输入框中输入需要处理的文本。
3. 节点将输出词元数量、自然语言描述和 CLIP 关键词。

## 依赖
- **spaCy**：用于自然语言处理。
- **en_core_web_sm**：spaCy 的英语小型模型。

如果和pulid冲突
卸载重装指定版本的库就可以解决
.\python.exe -m pip install numpy==1.26.4

## 安装
确保在 ComfyUI 的 Python 环境中安装了 spaCy 和 en_core_web_sm 模型。

python（comfyui的python_embeded下面那个） -m pip install spacy
python（comfyui的python_embeded下面那个） -m spacy download en_core_web_sm

如果你比较懒，那么就双击运行dowunload.bat文件吧，大部分情况应该可以解决问题。

## 注意事项
- 确保 ComfyUI 使用的 Python 环境中已安装所有依赖。
- 输入文本应为英文，以便 spaCy 模型正确处理。

## 贡献
欢迎对该节点进行改进和扩展。如有任何问题或建议，请提交 issue 或 pull request。
---
