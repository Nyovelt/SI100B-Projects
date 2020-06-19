#=============================================================================#
#                       Homework 5: SKY PRIORITY                              #
#       SI 100B: Introduction to Information Science and Technology           #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 03/11/2020                           #
#=============================================================================#
# task2.py - write your code for task 2 here.

import copy


class passenger:
    def __init__(self, arrival_time, passenger_name, vip=False, chd = False, parent= False):
        self.arrival_time = int(arrival_time)
        self.passenger_name = str(passenger_name)
        self.vip = bool(vip)
        self.chd = bool(chd)
        self.parent = bool(parent)
        self.time = int(arrival_time)


    def __lt__(self, other):
        if self.time == other.time:
            return (self.vip)
        else:
            return self.time < other.time

    def __len__(self):
        return 1

    def getOn(self, time=-999):
        self.time = int(time)

    def getOnTime(self):
        return self.time

    def getTime(self):
        return self.arrival_time

    def setCHD(self, chd):
        self.chd = bool(chd)

    def isCHD(self):
        return self.chd

    def setPAR(self, par):
        self.parent = bool((par))

    def idPAR(self, par):
        return self.parent

    def isVip(self):
        return   self.vip

    def getName(self):
        return self.passenger_name

    def __str__(self):
        return "name: " + str(self.passenger_name) + ", arrival-time:  " + str(self.arrival_time) + " vip: " + str(self.vip) + " chd: " + str(self.chd) + " parent: " + str(self.parent) + " get-on-time: " + str(self.time)


def print_list(list):
    for i in range(len(list)):
        print(list[i])

flight_num, passenger_num, boarding_time = input().strip().split()
passenger_num = int(passenger_num)
boarding_time = int(boarding_time)

ordinary_lane_passenger_list = list()
priority_lane_passenger_list = list()

#经济舱
newline1 = input()
ordinary_lane_passenger_num = int(input().strip())
for i in range(ordinary_lane_passenger_num):
    passenger_arrival_time, passenger_name, passenger_filght_num = input().strip().split()
    if passenger_filght_num == flight_num:
        ordinary_lane_passenger_list.append(passenger(passenger_arrival_time, passenger_name, vip=0))
    if passenger_name[-3:] == "CHD":
        ordinary_lane_passenger_list[-1].setCHD(chd=1)
    if len(ordinary_lane_passenger_list) >=2  and (ordinary_lane_passenger_list[-2].isCHD()):
            ordinary_lane_passenger_list[-1].setPAR(par=1)
            ordinary_lane_passenger_list[-2].getOn(ordinary_lane_passenger_list[-1].getOnTime())

#头等舱
newline2 = input()
priority_lane_passenger_num = int(input().strip())
for i in range(priority_lane_passenger_num):
    passenger_arrival_time, passenger_name, passenger_filght_num = input().strip().split()
    if passenger_filght_num == flight_num:
        priority_lane_passenger_list.append(passenger(passenger_arrival_time, passenger_name, vip=1))
    if passenger_name[-3:] == "CHD":
        priority_lane_passenger_list[-1].setCHD(chd=1)
    if len(priority_lane_passenger_list)>=2 and (priority_lane_passenger_list[-2].isCHD()):
            priority_lane_passenger_list[-1].setPAR(par=1)
            priority_lane_passenger_list[-2].getOn(priority_lane_passenger_list[-1].getOnTime())

# print_list(ordinary_lane_passenger_list)
# print_list(priority_lane_passenger_list)

# print(ordinary_lane_passenger_list[1] < ordinary_lane_passenger_list[2])

bus_start_time = boarding_time
output = list()
priority_lane_passenger_wait_list = list()
ordinary_lane_passenger_wait_list = list()
while (passenger_num):
    # print(bus_start_time)
    # print_list(output)
    if len(output) == 0 :
        for i in range(len(priority_lane_passenger_wait_list)):
            priority_lane_passenger_list.insert(i,priority_lane_passenger_wait_list[i])
        for i in range(len(ordinary_lane_passenger_wait_list)):
            ordinary_lane_passenger_list.insert(i, ordinary_lane_passenger_wait_list[i])
        ordinary_lane_passenger_wait_list.clear()
        priority_lane_passenger_wait_list.clear()

    if len(ordinary_lane_passenger_list):
        if ordinary_lane_passenger_list[0].getOnTime() < bus_start_time:
            if (ordinary_lane_passenger_list[0].isCHD()):
                ordinary_lane_passenger_list[0].getOn(bus_start_time)
                ordinary_lane_passenger_list[1].getOn(bus_start_time)
            else:
                ordinary_lane_passenger_list[0].getOn(bus_start_time)
    if len(priority_lane_passenger_list):
        if priority_lane_passenger_list[0].getOnTime() < bus_start_time:
            if (priority_lane_passenger_list[0].isCHD()):
                priority_lane_passenger_list[0].getOn(bus_start_time)
                priority_lane_passenger_list[1].getOn(bus_start_time)
            else:
                priority_lane_passenger_list[0].getOn(bus_start_time)

    if (len(ordinary_lane_passenger_list) and len(priority_lane_passenger_list)):
        if (priority_lane_passenger_list[0] < ordinary_lane_passenger_list[0]):
            if len(output) == 19 and priority_lane_passenger_list[0].isCHD() :
                priority_lane_passenger_wait_list.append(priority_lane_passenger_list[0])
                priority_lane_passenger_list.pop(0)
                priority_lane_passenger_wait_list.append(priority_lane_passenger_list[0])
                priority_lane_passenger_list.pop(0)
            else:
                output.append(priority_lane_passenger_list[0])
                passenger_num -= 1
                priority_lane_passenger_list.pop(0)
        else:
            if len(output) == 19 and ordinary_lane_passenger_list[0].isCHD() :
                ordinary_lane_passenger_wait_list.append(ordinary_lane_passenger_list[0])
                ordinary_lane_passenger_list.pop(0)
                ordinary_lane_passenger_wait_list.append(ordinary_lane_passenger_list[0])
                ordinary_lane_passenger_list.pop(0)
            else:
                output.append(ordinary_lane_passenger_list[0])
                passenger_num -= 1
                ordinary_lane_passenger_list.pop(0)
    elif (len(ordinary_lane_passenger_list) == 0 and len(priority_lane_passenger_list) > 0):
            if len(output) == 19 and priority_lane_passenger_list[0].isCHD() :
                priority_lane_passenger_wait_list.append(priority_lane_passenger_list[0])
                priority_lane_passenger_list.pop(0)
                priority_lane_passenger_wait_list.append(priority_lane_passenger_list[0])
                priority_lane_passenger_list.pop(0)
            else:
                output.append(priority_lane_passenger_list[0])
                passenger_num -= 1
                priority_lane_passenger_list.pop(0)
    elif (len(ordinary_lane_passenger_list) >0 and len(priority_lane_passenger_list) == 0):
            if len(output) == 19 and ordinary_lane_passenger_list[0].isCHD() :
                ordinary_lane_passenger_wait_list.append(ordinary_lane_passenger_list[0])
                ordinary_lane_passenger_list.pop(0)
                ordinary_lane_passenger_wait_list.append(ordinary_lane_passenger_list[0])
                ordinary_lane_passenger_list.pop(0)
            else:
                output.append(ordinary_lane_passenger_list[0])
                passenger_num -= 1
                ordinary_lane_passenger_list.pop(0)
    elif (len(ordinary_lane_passenger_list) == 0 and len(priority_lane_passenger_list) == 0):
        pass



    if len(output):
        if (output[-1].getOnTime() - output[0].getOnTime() > 600):
            # print("here")
            tmp = copy.deepcopy(output[-1])
            output.pop()
            print(output[0].getOnTime() + 600, end=":")
            for i in output:
                print("", i.getName(), end="")
            print()
            bus_start_time = output[0].getOnTime() + 1200
            output.clear()
            if tmp.isVip():
                priority_lane_passenger_list.insert(0, tmp)
            else:
                ordinary_lane_passenger_list.insert(0, tmp)
            passenger_num +=1

    if len(output) == 20:
        print(output[-1].getOnTime(), end=":")
        for i in output:
            print("", i.getName(), end="")
        print()
        bus_start_time = output[-1].getOnTime() + 600
        output.clear()

if len(output):
    print(output[-1].getOnTime(), end=":")
    for i in output:
        print("", i.getName(), end="")
    print()

