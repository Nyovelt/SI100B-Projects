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
    def __init__(self, arrival_time, passenger_name, vip):
        self.arrival_time = int(arrival_time)
        self.passenger_name = str(passenger_name)
        self.vip = bool(vip)
        self.time = int(arrival_time)
    
    def __lt__(self, other):
        if self.time == other.time:
            return (self.vip)
        else:
            return self.time < other.time

    def __len__(self):
        return 1

    def getOn(self, time):
        self.time = int(time)

    def getOnTime(self):
        return self.time

    def getTime(self):
        return self.arrival_time

    def isVip(self):
        return   self.vip
    
    def getName(self):
        return self.passenger_name

    def __str__(self):
        return "name: " + str(self.passenger_name) + ", arrival-time:  " + str(self.arrival_time) + " vip: " + str(self.vip) + " get-on-time: " + str(self.time)

 
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

#头等舱
newline2 = input()
priority_lane_passenger_num = int(input().strip())
for i in range(priority_lane_passenger_num):
    passenger_arrival_time, passenger_name, passenger_filght_num = input().strip().split()
    if passenger_filght_num == flight_num:
        priority_lane_passenger_list.append(passenger(passenger_arrival_time, passenger_name, vip=1))

# print_list(ordinary_lane_passenger_list)
# print_list(priority_lane_passenger_list)

# print(ordinary_lane_passenger_list[1] < ordinary_lane_passenger_list[2])

bus_start_time = boarding_time
output = list()
while (passenger_num):
    # print_list(output)
    if len(ordinary_lane_passenger_list):
        if ordinary_lane_passenger_list[0].getTime() < bus_start_time:
            ordinary_lane_passenger_list[0].getOn(bus_start_time)
    if len(priority_lane_passenger_list):
        if priority_lane_passenger_list[0].getTime() < bus_start_time:
            priority_lane_passenger_list[0].getOn(bus_start_time)

    if (len(ordinary_lane_passenger_list) and len(priority_lane_passenger_list)):
        if (priority_lane_passenger_list[0] < ordinary_lane_passenger_list[0]):
            output.append(priority_lane_passenger_list[0])
            passenger_num -= 1
            priority_lane_passenger_list.pop(0)
        else:
            output.append(ordinary_lane_passenger_list[0])
            passenger_num -= 1
            ordinary_lane_passenger_list.pop(0)            
    elif (len(ordinary_lane_passenger_list) == 0 and len(priority_lane_passenger_list) > 0):
            output.append(priority_lane_passenger_list[0])
            passenger_num -= 1
            priority_lane_passenger_list.pop(0)
    elif (len(ordinary_lane_passenger_list) >0 and len(priority_lane_passenger_list) == 0):
            output.append(ordinary_lane_passenger_list[0])
            passenger_num -= 1
            ordinary_lane_passenger_list.pop(0)
    elif (len(ordinary_lane_passenger_list) == 0 and len(priority_lane_passenger_list) == 0):
        pass
    # print_list(output)
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
    # print(passenger_num)
    # print_list(ordinary_lane_passenger_list)
    # print_list(priority_lane_passenger_list)
    # print()
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
        

    







