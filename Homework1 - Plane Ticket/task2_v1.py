#=============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
#=============================================================================#
# task2.py - write your code for task 2 here.

from collections import OrderedDict

priority_lane_passenger_list_flag = 0
ordinary_lane_passenger_list_flag = 0

# 第一行输入
flight_num, passenger_num, boarding_time = input().strip().split()
passenger_num = int(passenger_num)
boarding_time = int(boarding_time)

# 经济舱
newline_1 = input()
ordinary_lane_passenger_num = int(input().strip())
if ordinary_lane_passenger_num == 0:
    ordinary_lane_passenger_list_flag = 3
_ordinary_lane_passenger_num = ordinary_lane_passenger_num
ordinary_lane_passenger_dic = dict()

for i in range(int(ordinary_lane_passenger_num)):
    passenger_arrival_time, passenger_name, passenger_filght_num = input().strip().split()
    if (passenger_filght_num != flight_num):
        _ordinary_lane_passenger_num -= 1
        # print("有内鬼")
    else:
        ordinary_lane_passenger_dic[passenger_name] = int(
            passenger_arrival_time)

ordinary_lane_passenger_num = _ordinary_lane_passenger_num
if ordinary_lane_passenger_num == 0:
    ordinary_lane_passenger_list_flag = 3
ordinary_lane_passenger_queue = OrderedDict(
    sorted(ordinary_lane_passenger_dic.items(), key=lambda x: x[1]))
ordinary_lane_passenger_list_name = list(ordinary_lane_passenger_queue.keys())
ordinary_lane_passenger_list_boardtime = list(
    ordinary_lane_passenger_queue.values())

# 商务舱
newline_2 = input()
priority_lane_passenger_num = int(input().strip())
if priority_lane_passenger_num == 0:
    priority_lane_passenger_list_flag = 3
_priority_lane_passenger_num = priority_lane_passenger_num
priority_lane_passenger_dic = dict()

for i in range(priority_lane_passenger_num):
    passenger_arrival_time, passenger_name, passenger_filght_num = input().strip().split()
    if (passenger_filght_num != flight_num):
        _priority_lane_passenger_num -= 1
        # print("有内鬼")
    else:
        priority_lane_passenger_dic[passenger_name] = int(
            passenger_arrival_time)

priority_lane_passenger_num = _priority_lane_passenger_num
if priority_lane_passenger_num == 0:
    priority_lane_passenger_list_flag = 3
priority_lane_passenger_queue = OrderedDict(
    sorted(priority_lane_passenger_dic.items(), key=lambda x: x[1]))
priority_lane_passenger_list_name = list(priority_lane_passenger_queue.keys())
priority_lane_passenger_list_boardtime = list(
    priority_lane_passenger_queue.values())

# print(ordinary_lane_passenger_list_name)
# print(ordinary_lane_passenger_list_boardtime)
# print(priority_lane_passenger_list_name)
# print(priority_lane_passenger_list_boardtime)

bus_start_time = boarding_time
time = bus_start_time
priority_lane_passenger_list_iter = 0
ordinary_lane_passenger_list_iter = 0
the_passenger_on_the_bus = 0

output = list()

if (ordinary_lane_passenger_list_flag > 1) and (priority_lane_passenger_list_flag > 1):
    pass
else:
    while (1):
        if (priority_lane_passenger_list_flag <= 1) and (ordinary_lane_passenger_list_flag > 1): #都在头等舱
            # print("only priority")
            if ((priority_lane_passenger_list_boardtime[priority_lane_passenger_list_iter] <= time) and (priority_lane_passenger_list_iter < priority_lane_passenger_num-1) and (priority_lane_passenger_list_flag == 0)):
                # print("if")
                the_passenger_on_the_bus += 1
                output.append(
                    priority_lane_passenger_list_name[priority_lane_passenger_list_iter])
                priority_lane_passenger_list_iter += 1
            elif ((priority_lane_passenger_list_iter == priority_lane_passenger_num - 1) and (priority_lane_passenger_list_flag == 0) and (priority_lane_passenger_list_boardtime[priority_lane_passenger_list_iter] <= time)):
                # print("elif")
                the_passenger_on_the_bus += 1
                output.append(
                    priority_lane_passenger_list_name[priority_lane_passenger_list_iter])
                priority_lane_passenger_list_flag = 1
        elif (ordinary_lane_passenger_list_flag <= 1) and (priority_lane_passenger_list_flag > 1): #都在经济舱
            # print("task 1")
            if (ordinary_lane_passenger_list_boardtime[ordinary_lane_passenger_list_iter] <= time) and (ordinary_lane_passenger_list_iter < ordinary_lane_passenger_num -1):
                # print("el-if")
                the_passenger_on_the_bus += 1
                output.append(
                ordinary_lane_passenger_list_name[ordinary_lane_passenger_list_iter])
                ordinary_lane_passenger_list_iter += 1
            elif (ordinary_lane_passenger_list_iter == ordinary_lane_passenger_num -1) and (ordinary_lane_passenger_list_flag == 0) and (ordinary_lane_passenger_list_boardtime[ordinary_lane_passenger_list_iter] <= time):
                # print("el-elif")
                the_passenger_on_the_bus += 1
                output.append(
                    ordinary_lane_passenger_list_name[ordinary_lane_passenger_list_iter]
                )
                ordinary_lane_passenger_list_flag = 1
        elif (ordinary_lane_passenger_list_flag <=1) and (priority_lane_passenger_list_flag <=1) :
            # print("task 2")
            if ((priority_lane_passenger_list_boardtime[priority_lane_passenger_list_iter] <= time) and (priority_lane_passenger_list_iter < priority_lane_passenger_num-1) and (priority_lane_passenger_list_flag == 0)):
                # print("if")
                the_passenger_on_the_bus += 1
                output.append(
                    priority_lane_passenger_list_name[priority_lane_passenger_list_iter])
                priority_lane_passenger_list_iter += 1
            elif ((priority_lane_passenger_list_iter == priority_lane_passenger_num - 1) and (priority_lane_passenger_list_flag == 0) and (priority_lane_passenger_list_boardtime[priority_lane_passenger_list_iter] <= time)):
                # print("elif")
                the_passenger_on_the_bus += 1
                output.append(
                    priority_lane_passenger_list_name[priority_lane_passenger_list_iter])
                priority_lane_passenger_list_flag = 1
            else:
                if (ordinary_lane_passenger_list_flag <= 1) :
                    if (ordinary_lane_passenger_list_boardtime[ordinary_lane_passenger_list_iter] <= time) and (ordinary_lane_passenger_list_iter < ordinary_lane_passenger_num -1):
                        # print("el-if")
                        the_passenger_on_the_bus += 1
                        output.append(
                            ordinary_lane_passenger_list_name[ordinary_lane_passenger_list_iter])
                        ordinary_lane_passenger_list_iter += 1
                    elif (ordinary_lane_passenger_list_iter == ordinary_lane_passenger_num -1) and (ordinary_lane_passenger_list_flag == 0) and (ordinary_lane_passenger_list_boardtime[ordinary_lane_passenger_list_iter] <= time):
                        # print("el-elif")
                        the_passenger_on_the_bus += 1
                        output.append(
                            ordinary_lane_passenger_list_name[ordinary_lane_passenger_list_iter]
                        )
                        ordinary_lane_passenger_list_flag = 1
        bus_start_time = time
        if (priority_lane_passenger_list_flag >= 1 and ordinary_lane_passenger_list_flag == 0):
            time = max(
                time, ordinary_lane_passenger_list_boardtime[ordinary_lane_passenger_list_iter])
        elif (ordinary_lane_passenger_list_flag >= 1 and priority_lane_passenger_list_flag==0):
            time = max(
                time, priority_lane_passenger_list_boardtime[priority_lane_passenger_list_iter])
        elif(ordinary_lane_passenger_list_flag == 0 and priority_lane_passenger_list_flag==0):
            time = max(time, min(priority_lane_passenger_list_boardtime[priority_lane_passenger_list_iter],
                                ordinary_lane_passenger_list_boardtime[ordinary_lane_passenger_list_iter]))


        # print(output)
        # print(time)
        # print(priority_lane_passenger_list_iter)
        # print(priority_lane_passenger_num)
        if (the_passenger_on_the_bus == 20):
            the_passenger_on_the_bus = 0
            print(str(bus_start_time) + ":", end="")
            time = bus_start_time +600
            for j in range(20):
                print(" " + str(output[j]), end="")
            print()
            output.clear()
        elif (ordinary_lane_passenger_list_flag >=1) and (priority_lane_passenger_list_flag >= 1) and (len(output) != 0):
            print(str(bus_start_time) + ":", end="")
            for j in range(len(output)):
                print(" " + str(output[j]), end="")
            print()
            output.clear()
            break
        elif (ordinary_lane_passenger_list_flag >= 1) and (priority_lane_passenger_list_flag >= 1) and (len(output) == 0):
            break
