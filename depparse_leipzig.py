'''
Depparse_leipzig: Leipzig Corpus Depparse with Stanza
功能:
	将经预处理的Leipzig语料库文件进行依存句法分析
用法:
	depparse(语料库目录, 结果保存目录, 移动处理过的语料库到)
例子:
	depparse('D:/input/','d:/result/','d:/done/')
'''

from pathlib import Path as __Path
import stanza as __stanza
from stanza.utils.conll import CoNLL as __conll
import datetime as __datetime
import os as __os
import shutil as __shutil

def depparse(input_path,result_path,finished_path):
	input_leipzig_path = __Path(input_path)
	result_conll_path = __Path(result_path)
	done_leipzig_path = __Path(finished_path)

	filelist = __os.listdir(input_leipzig_path)
	for filename in filelist:
		input_filename = input_leipzig_path.joinpath(filename)
		processed_filename = done_leipzig_path.joinpath(filename)

		with open(input_filename,mode='r',encoding='utf-8') as leipzig_file:
			leipzig_text = leipzig_file.read()

		nlp = __stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse',use_gpu=False,download_method=None)

		start_time = __datetime.datetime.now()
		nosents = leipzig_text.count('\n\n')
		print(f'Processing: {filename}. Sents: {str(nosents)} Start Time: {str(start_time)}')
		doc = nlp(leipzig_text)
		end_time = __datetime.datetime.now()
		time_duration_in_sec = end_time-start_time
		time_duration_in_sec = time_duration_in_sec.seconds
		speed = nosents/time_duration_in_sec
		print(f'Finished: {filename}. End Time: {str(end_time)}')
		print(f'Time duration: {str(end_time-start_time)}')
		print(f'Speed: {str(speed)} sent per second')
		res_conll_filename = result_conll_path.joinpath(f'{filename[:-3]}conll')
		__conll.write_doc2conll(doc,res_conll_filename)
		with open(f'{str(res_conll_filename)[:-5]}log',mode='w',encoding='utf-8') as stanza_log:
			stanza_log.write(f'Start-time: {str(start_time)}')
			stanza_log.write('\n')
			stanza_log.write(f'End-time: {str(end_time)}')
			stanza_log.write('\n')
			stanza_log.write(f'Time-duration: {str(end_time-start_time)}')
			stanza_log.write('\n')
			stanza_log.write(f'Speed: {str(speed)} sent per second')
			stanza_log.write('\n')
		__shutil.move(input_filename,processed_filename)
		del leipzig_text,leipzig_file,nlp,doc



