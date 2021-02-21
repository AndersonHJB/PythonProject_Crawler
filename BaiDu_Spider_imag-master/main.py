# -*- coding: utf-8 -*-
# @Author     ：AI悦创
# @DateTime   ：2019/9/15  10:12 
# @FileName   ：imagebaidu.PY
# @Function   ：百度图片抓取
# Development_tool   ：PyCharm
# <-------import data-------------->
from is_not_int import isinstance_int
from spider_1 import download_image
from mkdir_file import mkdir_file_function
import os
# <----------------------User_Input------------------->
# Python 对 int 类型没有最大限制（相比之下， C++ 的 int 最大为 2147483647，超过这个数字会产生溢出），
# 但是对 float 类型依然有精度限制。这些特点，除了在一些算法竞赛中要注意，在生产环境中也要时刻提防，
# 避免因为对边界条件判断不清而造成 bug 甚至 0day（危重安全漏洞）。
# 因为，在写这个时候，发现知识点：with 上下文管理器，所以课下之后去学，当然如果老师能讲一下就更好咯嘿嘿。不过还是靠自己比较好一些。

if __name__ == '__main__':
	try:
		# print('只能以30起步，30为间隔')之后想了想这是多余的，既然是30固定，那就不需要这个start_pn_num
		# start_pn_num = (input('start_pn_num:>'))
		mkpath = os.path.dirname(__file__)  # 获取当前文件夹的绝对路径
		mkdir_file_function(mkpath)
		print('30为间隔，以30的倍数来哦！')
		end_pn_num = input('end_pn_sum:>')
		end_pn_num = isinstance_int(end_pn_num)
		download_image(end_pn_num + 1)
		# print(end_pn_num)
	   # 间隔是固定的不需要间隔（因为是作业，所以我把一些想法写出来，望老师看看有没有什么不足的或不对的，辛苦啦）
		# download_image(end_pn_num)

	except Exception as e:
		print(f'错误:>{e}')
		end_pn_num = 100
		download_image(end_pn_num)







