'''
Leipzig_divid_and_space_for_stanza_depparse
功能:
	1. 为Stanza的依存句法分析做预处理
	2. 将一行一句型的leipzig语料库拆分成多个小语料库(以限制一次性内存消耗)
	3. 将小语料库中的一行一句处理为隔行一句(行间以空行分隔, 此为stanza要求)
准备:
	1. 输入的leipzig语料库必须是一行一句型
	2. 输入的leipzig语料库必须是100万行左右
用法:
	1. leipzigdns(被分解的leipzig完整语料库文件,保存位置,分割为多少份(若按行切分,则应为1),多少行分隔为一份)
例子:
	按句子数切分
	leipzigdns('d:/input/leipzig_en_news_2005.txt','d:/result/',1,100000)
	按份数切分
	leipzigdns('d:/input/leipzig_en_news_2005.txt','d:/result/',100)
'''

from pathlib import Path as __Path

def leipzigdns(input_filename,output_path,divide_num=1,*interval):
	full_leipzig_path = __Path(input_filename)
	spaced_div_leipzig_path = __Path(output_path)
	with open(full_leipzig_path,mode='r',encoding='utf-8') as full_leipzig_file:
		full_leipzig_lines = full_leipzig_file.readlines()
	div_leipzig_lines = []
	line_no = len(full_leipzig_lines)
	# 如果按照行数进行切分, 则直接切分; 如果按照份数切分, 则先计算每份的句子数
	if interval:
		interval = interval[0]
	else:
		interval = line_no//divide_num
	for i in range(0,line_no,interval):
		div_leipzig_lines.append(full_leipzig_lines[i:i+interval])
	
	# 替换每个文件段中的单个换行为两个换行
	seg_cnt = 0
	for seg in div_leipzig_lines:
		line_cnt = 0
		seg_cnt += 1
		for line in seg:
			seg[line_cnt] = line.replace('\n','\n\n')
			line_cnt += 1

	# 将每个文件段粘贴为一个文本
	div_leipzig_texts = []
	for seg in div_leipzig_lines:
		div_leipzig_texts.append(''.join(seg))

	# 保存每个文件段的文本为一个文件
	filename_cnt = 1
	for text in div_leipzig_texts:
		with open(spaced_div_leipzig_path.joinpath(f'{full_leipzig_path.name[:-4]}_{filename_cnt:05d}.txt'),mode='w',encoding='utf-8') as outfile:
			outfile.write(text)
		filename_cnt += 1

