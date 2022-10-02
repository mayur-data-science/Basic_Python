# Recursion in python

def factorial(num):
    if num == 1:
        return 1
    else:
                        # Calling function
        return num   *  factorial(num-1)    # return 5 * factorial(4)       # return 5 * 24 # return 120
                                                        # Calling function
                                            # return 4 * factorial(3)       # return 4 * 6  # return 24
                                                        # Calling function
                                            # return 3 * factorial(2)       # return 3 * 2  # return 6
                                                        # Calling function
                                            # return 2 * factorial(1)       # return 2 * 1  # return 2
                                            #               if True     # else bolc wont run bcz "if" conditon evaluates "True" so no function call again.
                                                                # return 1
num1 = 5
result = factorial(num1) # calling function # result = 120
print(result) # 120

# 
#  sequence pattern

def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [first, *rest]:
            return first + sum_list(rest)
a=sum_list([4, 5, 9, 17])
print(a) # o/p : 35