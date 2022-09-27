# depparse_stanza工具集
## 功能
1. 将一行一句型文本处理成适合stanza进行处理的隔行一句型文本 divide_leipzig.py
2. 将大文本分隔成多个小文本 divide_leipzig.py
3. 使用Stanza对按照上边两步处理的文本们进行依存句法分析 depparse_leipzig.py
4. 重排一个目录中的CONLL文件的 sent_id项目 reorder_sentid.py
## 依赖
1. STANZA和英文语言包
## 用法
1. 在每个模块的帮助文档中
2. 创建一个RESULT文件夹用于存储depparse_leipzig的输出
3. 创建一个SPLIT文件夹用于存储divide_leipzig的输出
4. 创建一个RECORDERED文件夹用于存储reorder_sentid的输出