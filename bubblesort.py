import random

scattered_list = [random.randint(1,10) for _ in range(10)]


for i in range(len(scattered_list)):

    for i in range(len(scattered_list)-1):

        if scattered_list[i] > scattered_list[i+1]:

                scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]
                print(scattered_list)