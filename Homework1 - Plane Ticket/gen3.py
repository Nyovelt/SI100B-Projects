import random


# for i in range(30):
#         print(1200*i + i*i,i,"MU2333")

# print(random.random())

a = int(200 * random.random())
b = int(200 * random.random())

time = int(2000 * random.random())

print("MU2333", a+b, time)

delta = 5000

time = 0

print()
print(a)
for i in range(a):
        time += int(delta * random.random())
        print(time, i + 1, "MU2333")

time = 0     
print()
print(b)
for i in range(b):
        time += int(delta * random.random())
        print(time, i+1, "MU2333")