import random

time = int(200 * random.random())

print("MU233" + " " + "123" + " " + str(time))

print()


num = 30

print(num)

tuple = tuple()

for i in range(num):
    time = str(int(random.random() * 5 * num))
	
    if (random.random() <= 0.05):
        print(time + " " + time + " " + "MU888")
    else:
        print(time + " " + time + " " + "MU233")
