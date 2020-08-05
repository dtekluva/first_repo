# def bla(*a):# variable positional arguments
#     print(a)

# bla(3, 3, 4, 576, 67, 8, 89, 8, 45)


# def key_word_func(a,b,c):
#     print("a =", a,"b =", b, "c =", c)

# key_word_func("b", "c", "a")
# key_word_func(b = "b", c = "c",  a ="a")

# def students(**data): # variable keyword arguments
#     print(data.values())

# students(ade=23, bolu=12, shade=54, sean=50)


# def products(**data): # variable keyword arguments
#     for key in data:
#         print(key, ":", data[key])

#     prices = sum(data.values())
#     print("Total :", prices )

# products(oil=23, rice=12, greens=54, garri=50)

# def sort_values(*scattered_list, should_be_ascending = True):

#     scattered_list = list(scattered_list)

#     for i in range(len(scattered_list)):

#         for i in range(len(scattered_list)-1):

#             if scattered_list[i][1] > scattered_list[i+1][1]:

#                     scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]
    
#     if should_be_ascending:
#         print(scattered_list)
#     else:
#         print(scattered_list[::-1])


# # sort_values(2,1,4,7,1,2,4,2,5,67,12, should_be_ascending=False)

# def string_processor(string):
#     string = string.lower()
#     unique_values = list(set(string))
#     quantities = []
    
#     for value in unique_values:
#         quantities.append(string.count(value))
    
#     zipped_vals = list(zip(unique_values,quantities))
    
#     sort_values(*zipped_vals, should_be_ascending=False)

    

# string_processor("I have a dream, a song to sing. To help me cope")

# def xyz():
#     print(1)

# # print(xyz())
# answer = xyz()
# print(answer)

def tri_recursion(k):
    if(k > 0):
        x = tri_recursion(k - 1)
        result = k + x
        print(k, x, result)
    else:
        result = 0
        print(result)
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
