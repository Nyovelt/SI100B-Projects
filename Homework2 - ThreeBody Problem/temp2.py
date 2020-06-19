import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as npy
import random

from math import sqrt, pi, sin, cos
import copy
ERROR = 0.01
G = 1
planet_list = list()
colors=["r", "g", "b","r","g","b"]

def AlmostEqual(first, second):
    delta = abs(ERROR * first)
    diff = abs(first - second)
    assert diff <= delta
    
def dot_product(x_1, y_1, x_2, y_2):
    return x_1*x_2 + y_1*y_2

def angle(x_1, y_1, x_2, y_2):
    return 

def F(m_1, m_2, d_x, d_y):
    ''' Newton's Law of Universe Gravitation '''
    r = sqrt(d_x * d_x + d_y * d_y)
    if r == 0:
        # print("yo")
        return [0,0]
    else:
        tmp = -G * m_1 / r * m_2 / r 
        return [tmp*d_x/r, tmp*d_y/r]
        
class planet:
    def __init__(self, mass, coordinate_x, coordinate_y, speed_x, speed_y):
        self.mass = (mass)
        self.coordinate_x = (coordinate_x)
        self.coordinate_y = (coordinate_y)
        self.speed_x = (speed_x)
        self.speed_y = (speed_y)
        self.x_list = list()
        self.y_list=list()

    def __str__(self):
        return "mass: " + str(self.mass) + " coordianate-x: " + str(self.coordinate_x) + " coordiante-y: " + \
            str(self.coordinate_y) + " speed-x: " + str(self.speed_x) + " speed-y: " + str(self.speed_y)
    
    def renew(self, list: list):
        force = [0,0]
        for i in list:
            delta_force = F(self.mass, i.mass
                , self.coordinate_x - i.coordinate_x, self.coordinate_y - i.coordinate_y)
            force[0] += delta_force[0]
            force[1] += delta_force[1]
        self.speed_x += force[0] / self.mass
        self.speed_y += force[1] / self.mass
        self.coordinate_x += self.speed_x
        self.coordinate_y += self.speed_y
        self.x_list.append(self.coordinate_x)
        self.y_list.append(self.coordinate_y)

    def draw(self):
        #创建图并命名
        plt.figure('Line fig')
        ax = plt.gca()
        #设置x轴、y轴名称
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        #画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
        #参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
        ax.plot(self.x_list, self.y_list, color=colors[int(random.random()*6)], linewidth=1, alpha=0.6)

def print_list(list):
        for i in list:
                print(str(i))

def task1(planets_num: int, check_time: int, bodys: list):
    for i in range(planets_num):
        planet_list.append(planet(bodys[i][0], bodys[i][1], bodys[i][2], bodys[i][3], bodys[i][4]))
    # print_list(planet_list)
    pre_planet_list = list()
    for i in range(check_time):
        pre_planet_list = copy.deepcopy(planet_list)
        for j in planet_list:
            j.renew(pre_planet_list)
        pre_planet_list.clear()
    for i in planet_list:
        i.draw()
    plt.savefig('./planet.png')
    # print_list(planet_list)
    # print([[i.coordinate_x, i.coordinate_y] for i in planet_list])
    return [[i.coordinate_x, i.coordinate_y] for i in planet_list]

# task1(
#     2,
#     1986,
#     [
#         [10000, 0, 0, 0, 0],
#         [0.1, 1000, 0, 0, sqrt(10)] #[planet1_mass, planet1_coordinate_x, planet1_coordinate_y,
#          # planet1_speed_x, planet1_speed_y]
#     ]
# )

# print(F(2,1,sqrt(2),sqrt(2)))