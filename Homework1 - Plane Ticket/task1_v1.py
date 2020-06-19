#=============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
#=============================================================================#
# task1.py - write your code for task 1 here.

from collections import OrderedDict

flight_num, passenger_num, boarding_time = input().strip().split()

test = input()
ordinary_lane_passenger_num = input().strip()

passenger_num = int(ordinary_lane_passenger_num)
boarding_time = int(boarding_time)
_passenger_num = passenger_num
dic = dict()

for i in range(int(passenger_num)):
    passenger_arrival_time, passenger_name, passenger_filght_num = input().strip().split()
    if (passenger_filght_num != flight_num):
        _passenger_num -= 1
        # print("有内鬼")
    else:
        dic[passenger_name] = int(passenger_arrival_time)

passenger_num = _passenger_num
queue = OrderedDict(sorted(dic.items(), key=lambda x: x[1]))
# print(queue)
list_passenger_name = list(queue.keys())
list_arrival_time = list(queue.values())

bus_time = int(boarding_time)
bus_ptr = 0



if (passenger_num <= 0):
    print()
elif (0 < passenger_num <= 20): #如果小于20人则判断
    if (list_arrival_time[passenger_num - 1] < boarding_time):
        print(str(boarding_time) + ":", end="")
        for i in range(passenger_num):
            print(" " + list_passenger_name[i], end="")
        print()
    else:
        print(str(list_arrival_time[passenger_num-1]) + ":", end="")
        for i in range(passenger_num):
            print(" " + list_passenger_name[i], end="")
        print()
else: #大于20人的情况
    while (1):
        if (bus_ptr + 20 >= passenger_num):
            print(
                str(max(list_arrival_time[passenger_num-1], bus_time)) + ":", end="")
            for i in range(passenger_num-bus_ptr):
                print(
                    " " + list_passenger_name[i + bus_ptr], end="")
            print()
            break

        print(
            str(max(bus_time, list_arrival_time[bus_ptr + 19])) + ":", end="")
        for i in range(20):
            print(" " + list_passenger_name[i + bus_ptr], end="")
        print()
        bus_time = max(list_arrival_time[bus_ptr+19] ,bus_time+10)
        bus_ptr += 20
        # bus_time = max(bus_time, list_arrival_time[bus_ptr + 19])+10
        if (bus_ptr + 20 >= passenger_num):
            bus_time = max(bus_time, list_arrival_time[passenger_num - 1])
        else:
            bus_time = max(bus_time, list_arrival_time[bus_ptr + 19])

        # print("bus_time:",bus_time)
