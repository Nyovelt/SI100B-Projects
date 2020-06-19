# import matplotlib
# matplotlib.use('agg')
# import matplotlib.pyplot as plt
# import numpy as npy
# import random

from math import sqrt, pi, sin, cos, pow
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
    # print(x_1*x_2 + y_1*y_2)
    return x_1*x_2 + y_1*y_2

def angle(x_1, y_1, x_2, y_2):
    return
    
def distance(x_1, y_1, x_2, y_2):
    # print(sqrt((x_1-x_2)*(x_1-x_2) + (y_1-y_2)*(y_1-y_2)))
    return sqrt((x_1-x_2)*(x_1-x_2) + (y_1-y_2)*(y_1-y_2))

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
        # self.x_list = list()
        # self.y_list=list()

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
        # self.x_list.append(self.coordinate_x)
        # self.y_list.append(self.coordinate_y)

'''
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
'''

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
        # pre_planet_list.clear()
#     for i in planet_list:
#         i.draw()
#     plt.savefig('./planet.png')
    #print_list(planet_list)
#     print([[i.coordinate_x, i.coordinate_y] for i in planet_list])
    return [[i.coordinate_x, i.coordinate_y] for i in planet_list]


def task2(check_time: int, bodys: list):
    tmp = task1(4, check_time, bodys)
    # print_list(planet_list)
    # print(tmp)   
    sun = 0
    for i in range(3):
            if (distance(tmp[i][0], tmp[i][1], tmp[3][0], tmp[3][1]) <= 200):
                    sun+=1
    if sun == 0:
        return "Eternal Night"
    elif sun == 1:
        return "Stable Era"
    elif sun == 2:
        return "Double-Solar Day"
    elif sun == 3:
        return "Tri-Solar Day"

def task3(check_time: int, bodys: list):
    S = 0
    for i in range(4):
        planet_list.append(planet(bodys[i][0], bodys[i][1], bodys[i][2], bodys[i][3], bodys[i][4]))
    pre_planet_list = list()
    for i in range(check_time):
        pre_planet_list = copy.deepcopy(planet_list)
        for j in planet_list:
            j.renew(pre_planet_list)
        pre_planet_list.clear()
        sun = 0
        for j in range(3):
            if (distance(planet_list[j].coordinate_x, planet_list[j].coordinate_y, planet_list[3].coordinate_x, planet_list[3].coordinate_y)
                <= 200):
                sun += 1
        if sun == 1:
            S += 2
        elif sun == 0 or sun == 2 or sun == 3:
            S -= 1
        if S < 0:
            return "No civilization"

    if S < 0:
        return "No civilization"
    elif S < 400:
        return "level 1 civilization"
    elif S < 1200:
        return "level 2 civilization"
    else:
        return "level 3 civilization"

def task_bonus(check_time: int, bodys: list):
    day = 0
    for i in range(4):
        planet_list.append(planet(bodys[i][0], bodys[i][1], bodys[i][2], bodys[i][3], bodys[i][4]))
    for i in range(check_time):
        tmp = i % 360
        position = [sin(tmp / 360 * 2 * pi), cos(tmp / 360 * 2 * pi)]
        pre_planet_list = list()
        pre_planet_list = copy.deepcopy(planet_list)
        for j in planet_list:
            j.renew(pre_planet_list)
        sun  =0
        for j in range(3):
            if (distance(planet_list[j].coordinate_x, planet_list[j].coordinate_y, planet_list[3].coordinate_x, planet_list[3].coordinate_y)
            <= 200):
                sun += 1
        if sun != 1:
            continue
        sun_on_the_head = 0
        for j in range(3):
            if dot_product(position[0], position[1], planet_list[j].coordinate_x - planet_list[3].coordinate_x,
                planet_list[j].coordinate_y - planet_list[3].coordinate_y) >= 0:
                sun_on_the_head +=1 
        if sun_on_the_head == 3:
            day += 1
        
    # print_list(planet_list)
    return day

omega = 2*pi/360
R = (1000/omega**2)**(1/3)
output = task_bonus(
        6000,
        [
            [1000, 0, 0, 0, 0],
            [0.001, R, 0, 0, -omega*R],
            [0.001, 0, R, omega*R, 0],
            [0.001, 0, -R, -omega*R, 0]
        ]
)

print(output)
