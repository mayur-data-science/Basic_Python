#Recurtion in python

def factorial(num):
    if num == 1:
        return 1
    else:
                        # Calling function
        return num   *  factorial(num-1)    # return 5 * factorial(4)  # 5 * 24 # return 120
                                            # return 4 * factorial(3)  # 4 * 6  # return 24
                                            # return 3 * factorial(2)  # 3 * 2  # return 6 
                                            # return 2 * factorial(1)  # 2 * 1  # return 2
                                            #               if True     # else bolc wont run bcz if conditon evaluates True so no function call again.
                                                                # return 1
num1 = 5
result = factorial(num1) # calling function # result = 120
print(result) # 120