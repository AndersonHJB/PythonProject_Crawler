import re
import requests
import webbrowser
import tkinter as tk
url = "http://www.qmaile.com/"
response=requests.get(url)
#解析
response.encoding='utf-8'
#网页源代码
responsed = response.text
#正则表达式匹配所需接口
rg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(rg,responsed)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]

#窗口
root = tk.Tk()
root.geometry('500x250')#调整大小
root.title('vip_movie')
l1 = tk.Label(root,text='播放接口：',font=12)#创建标签
l1.grid(row = 0,column=0)#显示标签
var = tk.StringVar()

r1 = tk.Radiobutton(root,text='播放接口1',variable=var,value=one,font=12)
r1.grid(row = 0,column=1)#摆放位置
r2 = tk.Radiobutton(root,text='播放接口2',variable=var,value=two,font=12)
r2.grid(row = 1,column=1)
r3 = tk.Radiobutton(root,text='播放接口3',variable=var,value=three,font=12)
r3.grid(row = 2,column=1)
r4 = tk.Radiobutton(root,text='播放接口4',variable=var,value=four,font=12)
r4.grid(row = 3,column=1)
r5 = tk.Radiobutton(root,text='播放接口5',variable=var,value=five,font=12)
r5.grid(row = 4,column=1)

l2  = tk.Label(root,text='播放链接：',font=12)
l2.grid(row=5,column=0)

#输入框
e1=tk.Entry(root,text='',width='50')
e1.grid(row=5,column=1)
#两个按钮和功能函数

def bf():
	webbrowser.open(var.get()+e1.get())
def qc():
	e1.delete(0,'end')
f1 = tk.Button(root,text='播放',font=12,width = 8,command=bf)
f1.grid(row=7,column=1)
f1 = tk.Button(root,text='清除',font=12,width = 8,command=qc)
f1.grid(row=8,column=1)
root.mainloop()#刷新窗口


