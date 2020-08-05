import random

data = []


reference = [random.randint(1,5) for i in range(7)]
reference_copy = reference.copy()

temp_list = []

for j in range(5):

    for i in range(len(reference)):
        if reference[i] > 0:
            temp_list.append("#")
        else:
            temp_list.append(" ")
        
        reference[i] -= 1
            

    data.append(temp_list)
    temp_list = []

for line in reversed(data):
    print(" | ".join(line))
print()


reference = sorted(reference_copy)
# print(reference)

temp_list = []
data = []

for j in range(5):

    for i in range(len(reference)):
        if reference[i] > 0:
            temp_list.append("#")
        else:
            temp_list.append(" ")
        
        reference[i] -= 1
            

    data.append(temp_list)
    temp_list = []

for line in reversed(data):
    print(" | ".join(line))