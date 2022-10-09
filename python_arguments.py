# Python Arguments :

#----------------------------------------------------------------------------------------------------------

### Parameters: 
        # A parameter is the variable defined within the parentheses during function definition. 
        # Simply they are written when we declare a function. 

# Ex : 1

def sum(a,b): # Here a,b are the parameters
    print(a+b)
    
sum(1,2)
#----------------------------------------------------------------------------------------------------------

### Arguments:
        # An argument is a data that is passed to a function when it is called. 
        # Data might be a callable function, string, int, float, boolean(True or False) as input. 
        # They are written in the function call.

# Ex : 1

def sum(a,b):
    print(a+b)
    
sum(1,2) # Here the values 1,2 are arguments

# Ex : 2
def sum(a,b): 
    print("a is : ", a)
    print("b is : ", b)
    print(a==b)
sum(1,True) # passing boolean data
# in python "1" is considered as "True" and "0", negative, positive integer, is considered as "False".
# o/p :
        # a is :  1
        # b is :  True
        # True
#----------------------------------------------------------------------------------------------------------------

### Positional Arguments :

        # Positional Arguments are needed to be included in proper order
        # i.e the first argument is always listed first when the function is called, 
        # second argument needs to be listed second when function is called and so on....
        
# Ex : 1

def person_name(first_name,second_name):
    print(first_name + second_name)
	
person_name("Ram","Babu")   # First name is Ram placed first
                            # Second name is Babu place second while calling a function.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Keyword Arguments:
        # Keyword Arguments is an argument passed to a function or method which is preceded by a keyword and an equal to sign.
        # The order in keyword Arguments need not to be same as in positional argument.
        # while calling a function we explicitly telling python which argument value goes to which parameters in function declation by keyword names same as given in parameters.

# Ex : 1

def person_name(first_name,second_name):
    print(first_name + second_name)

person_name(second_name="Babu",first_name="Ram") # Here we are explicitly assigning the value. # order dosent matter
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Positional Arguments & Keyword Arguments in same function:
        
        # if we specify positional argument and  Keyword Arguments in same function its mandatory that 
        # we must specify "positional Arguments" "first" and then specify Keyword Arguments.
        # other wise we will get syntaxError.

# Ex : 1

def fruits(a, b, p): # Non-default Parameters. # mandatory to pass 3 argument while calling this function.
    print('We have', a+ ',', b+ ' and', p+ ' at our store.')

fruits('apple', 'banana', 'pineapple') # Positional Arguments. # order matters while calling.

fruits(a = 'apple', b = 'banana', p = 'pineapple') # Keyword Arguments # order doesn't matters while calling.

fruits(b = 'banana', p = 'pineapple', a = 'apple') # Keyword Arguments not in order 

fruits('apple', b = 'banana', p = 'pineapple')  # two Keyword Argument, one Positional Argument.
                                                # Positional Arguments must be first.

# fruits(b = 'banana', p = 'pineapple', 'apple')# SyntaxError: positional argument follows keyword argument.
# fruits('apple', b = 'banana', 'pineapple') # SyntaxError: positional argument follows keyword argument.

#-------------------------------------------------------------------------------------------------------------------------------------------------

### Python Default and Non-default Parameters:

    #   Function parameters have default data assigned to them. (data can be callable function, string, int, float, boolean(True or False) )
    #   This can be done by using the assignment operator (=) in the function parameter. 
    #   When a function is called without an argument, the default data is used from parameter inside function. 
    #   This is useful when someone forgets to pass an argument while calling function and executes the program.
    #   default arguments(parameter) , must be followed by Non-default arguments(parameter).
    #   means we must write positional argument first, then deafult argument

    # Note – Python Default arguments are also called as Python Optional arguments.
    #        its not mandatory to pass default or optional argument while calling a function.
    #        if we provide default argument while calling function, the dafault data will not be utilized from function parameter.(overridding deafult data)
    #        if we dont provide default argument while calling function, the default data will be utilized from function parameter.

# Ex 1: 
def welcome(fullname, msg = 'Welcome to python!!'): # fullname is Non-Default parameter and msg is Default parameter.
    print('Hey there', fullname + ', ' + msg) # If the msg argument is not provided while calling function, then the default data from the function parameter is utilized.

welcome('Sam')  # Here we are only passing one positional argument which is mandatory for function call. 
                # and we are not passing second argument which is "optional(default) argument" while calling function
                # while calling a function its mandatory to pass argument in same order which defined in function declaration as parameter.
welcome('Zack', 'How have you been?') # 2nd argument data passed as a string, welcome function will not use its default parameter data.

# o/p: 
    # Hey there Sam, Welcome to python!!
    # Hey there Zack, How have you been?


# Ex: 2
# default parameter having callable function.
def add_str():
    return "You Are Awesome"

def welcome(fullname, msg = add_str): # fullname is positional parameter and msg is default parameter having dafult data which is callable function.
    if callable(msg) == True:
        print("Hey there {0}, {1}".format(fullname, msg()))
    else:
        print(f"Hey there {fullname}, Your age is {msg}")
        
        
welcome('Sam')  # Here we are only passing one positional argument which is mandatory. 
                # and we are not passing second argument which is "optional argument" while calling function
welcome('Zack',28)

# o/p:
    # Hey there Sam, You Are Awesome
    # Hey there Zack, Your age is 28


# Ex: 3
    # Non-default arguments, cannot be followed by default arguments.

# def function(a = 24, b, c): # SyntaxError: non-default argument follows default argument
# def function(b,a=24,c) # SyntaxError: non-default argument follows default argument
def function(b,c, a= 24,): # valid
    print('Values are:')
    print(a)
    print(b)
    print(c)

function(10, 4)

# Ex: 4
def adder(x,y,z):
    print("sum:",x+y+z)

adder(5,10,15,20,25)
# o/p: TypeError: adder() takes 3 positional arguments but 5 were given

#--------------------------------------------------------------------------------------------------------------------------------
###### To solve this problem (*args and **kwargs (Arbitrary Arguments) concept is impotant to learn)######
#--------------------------------------------------------------------------------------------------------------------------------


# Python Arbitrary Arguments :

# *args :
    # In this, we use the asterisk (*) to denote that perticular function only accept positional argument in function parameter. 
    # This is also called as Python *args. 
    # Python "*args" allows a function to "accept any number of positional arguments" passed while calling function
    # i.e. arguments which are non-keyword arguments, accepts variable-length(means no argument or less or more argument) while calling function.

    # Remember 'args' is just a notation. We can use any other argument name instead of it.

# Ex: 1.0
def adder(*args):   # accepts only positional arguments in the form of tuple
    print("Tuple:",args)

adder(a=5,b=10,c=15,d=20,e=25) # TypeError: adder() got an unexpected keyword argument 'a'

# Ex: 1.1
def adder(*args):   # accepts arguments in the form of tuple
    print("Tuple:",args)

adder(5,10,15,20,25)    # o/p: Tuple: (5, 10, 15, 20, 25)
    
# Ex: 1.2
def adder(*args):   # accepts arguments in the form of tuple
    # a,b,c,d,e = *args # SyntaxError: can't use starred expression here
    print("Unpacked data:",*args) # print is also a function  # so we can use  *args

adder(5,10,15,20,25)    # o/p: Unpacked data: 5 10 15 20 25


# Ex: 1.3
def adder(*args): # args = (5,10,15,20,25) # accepts arguments in the form of tuple
    a,b,c,d,e = args # Unpacking each data from tuple and assign it to respective variable
    # a,b,c,d,e = *args # SyntaxError: can't use starred expression here
    # a, b, c, d = args # ValueError: too many values to unpack (expected 4) # values and variables must match
    # a, b, c, d, e, f = args # ValueError: not enough values to unpack (expected 6, got 5) # values and variables must match
    print("sum:",a+b+c+d+e)

adder(5,10,15,20,25) # o/p: 75


# Ex: 2
def my_sum_of_list(*args):
    result = 0
    for x in args: # for x in (10,20,30,40,50,60,70,80,90) # iterating over each element in tuple
        result += x
    return result

list1 = [10, 20, 30]
list2 = [40, 50]
list3 = [60, 70, 80, 90]

print(my_sum_of_list(*list1, *list2, *list3)) # unpacking list data first
# o/p: 450




    # **kwargs :
        # In this, we use the asterisk (**) to denote that perticular function only accept Keyword argument in function parameter.
        # This is also called as Python **kwargs.
        # Python "**kwargs" allows a function to "accept any number of Keyword arguments" passed while calling function
        # i.e. arguments which are keyword arguments, accepts variable-length(means no argument or less or more argument) while calling function.

# arbitrary arguments come in handy when we don’t know how many arguments needed to pass in the function or method at that moment.

# Ex 1:


