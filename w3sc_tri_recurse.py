# def tri_recursion(k):
#   print(k)
#   if(k > 0):
#     result = k + tri_recursion(k - 3)
#     # print(result)
#   else:
#     result = 0

#   print(k, result)
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(9)


# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = 8
# print("The factorial of", num, "is", factorial(num))

# def FibRecursion(n):  
#    if n <= 1:  
#        return n  
#    else:  
#        return(FibRecursion(n-1) + FibRecursion(n-2))  
# nterms = int(input("Enter the terms? "))  # take input from the user
  
# if nterms <= 0:  # check if the number is valid 
#    print("Please enter a positive integer")  
# else:  
#    print("Fibonacci sequence:")  
#    for i in range(nterms):  
#        print(FibRecursion(i))

_list = [3,4,8,22,34,54,60]

_list = input("Please enter nos seperated by comma : ")
print(_list)
_list = _list.split(",")
print(_list)
_list = list(map(lambda string: int(string), _list))
print(_list)

def moving_difference(_list, differences = []):

    if len(_list) < 2:
        return differences
    else:
        differences.append(_list[1] - _list[0])
        return moving_difference(_list[1:], differences)

print(moving_difference(_list))
 