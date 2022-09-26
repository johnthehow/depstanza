'''
depparse_stanza工具集
功能:
	1. 将一行一句型文本处理成适合stanza进行处理的隔行一句型文本 divide_leipzig.py
	2. 将大文本分隔成多个小文本 divide_leipzig.py
	3. 使用Stanza对按照上边两步处理的文本们进行依存句法分析 depparse_leipzig.py
	4. 重排一个目录中的CONLL文件的 sent_id项目 reorder_sentid.py
'''

__all__ = ['divide_leipzig','depparse_leipzig','reorder_sentid']

from depparse_stanza import divide_leipzig
from depparse_stanza import depparse_leipzig
from depparse_stanza import reorder_sentid