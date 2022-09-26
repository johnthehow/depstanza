'''
Reorder_sentid: Re-order the # sent_id in CONLL file

Prepare:
	把要重新编号的所有CONLL文件放进一个文件夹(source path)
	编号顺序按照os.listdir()中的文件顺序
	句子编号从1到n递增
	结果保存到另一个文件夹(save path)
Usage:
	reorder(source_path,save_path,startid)
		Parameters:
			source_path: 包含所有CONLL文件的文件夹
			save_path: 重新编号sentid后的CONLL文件的存放文件夹
			startid: 重新编号时的起始编号
Example:
	reorder('D:/conll/','D:/save/',10000)
'''

import re as __re
from pathlib import Path as __Path
import os as __os

def reorder(source_path,save_path,startid):
	# 设置输入和结果保存目录
	source_path = __Path(source_path)
	save_path = __Path(save_path)

	# 获得输入目录文件列表, 选择CON
	source_file_list = __os.listdir(source_path)
	source_file_list = [i for i in source_file_list if i.endswith('conll')]

	# 总句数计数器, 累加各个文件中的句子数, 直到整个文件夹遍历完
	total_sent_cnt = startid
	for filename in source_file_list:
		source_file_path = source_path.joinpath(filename)
		with open(source_file_path,mode='r',encoding='utf-8') as file:
			lines = file.readlines()
		line_cnt = 0
		# 张开一个列表, 避免append方法速度缓慢
		res = ['place_holder']*len(lines)
		# 修改 sent_id后的句子编号
		for line in lines:
			if line.startswith('# sent_id'):
				num = __re.search('\d+',line).group()
				int_num = int(num)
				sub = str(int_num+1)
				new_line = f'# sent_id = '+str(total_sent_cnt)+'\n'
				res[line_cnt]= new_line
				line_cnt += 1
				total_sent_cnt += 1
			else:
				res[line_cnt] = line
				line_cnt += 1
		save_filename = save_path.joinpath(filename)
		with open(save_filename, mode='w+', encoding='utf-8') as file:
			file.write(''.join(res))
