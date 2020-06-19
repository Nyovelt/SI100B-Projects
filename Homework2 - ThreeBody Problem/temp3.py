import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import random
colors=["r", "g", "b"]
#分别存放所有点的横坐标和纵坐标，一一对应
x_list = [1,2,3]
y_list = [2,3,4]

#创建图并命名
plt.figure('Line fig')
ax = plt.gca()
#设置x轴、y轴名称
ax.set_xlabel('x')
ax.set_ylabel('y')

#画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
#参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
ax.plot(x_list, y_list, color='r', linewidth=1, alpha=0.6)
#分别存放所有点的横坐标和纵坐标，一一对应
x_list = [5,6,7]
y_list = [2,3,4]

#创建图并命名
plt.figure('Line fig')
ax = plt.gca()
#设置x轴、y轴名称
ax.set_xlabel('x')
ax.set_ylabel('y')

#画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
#参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
ax.plot(x_list, y_list, color=colors[int(random.random()*2)], linewidth=1, alpha=0.6)
plt.savefig('./test.png')



