                                #---------------------------------#
                                # Python Parameters and Arguments :
                                #---------------------------------#

#----------------------------------------------------------------------------------------------------------

#-----------#
# Parameters:
#-----------#
        # A parameter is the variable defined within the parentheses during function definition. 
        # Simply they are written when we declare a function. 

# Ex : 1

def sum(a,b): # Here a,b are the parameters
    print(a+b)
    
sum(1,2)

#----------------------------------------------------------------------------------------------------------

#----------#
# Arguments:
#----------#

        # An argument is a data that is passed to a function when it is called. 
        # Data might be a callable function, string, int, float, boolean(True or False), complex as input. 
        # They are written in the function call.

# Ex : 1

def sum(a,b):
    print(a+b)
    
sum(1,2) # Here the data 1,2 are arguments

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

# Ex : 3

def sum(a,b):
    print(a+b)
    print(type(a))
    print(type(b))
    
sum(1,10+20j) # passing int and complex data as an arguments to function.

    # o/p : 
        # (11+20j)
        # <class 'int'>
        # <class 'complex'>

#----------------------------------------------------------------------------------------------------------------
#--------------------#
# Standard Arguments :
#--------------------#


    #----------------------#
    # Positional Arguments :
    #----------------------#
            # Positional arguments are arguments that need to be included in the proper position or order.
            # Positional Arguments are always be defined first in function declaration
            # i.e the first argument is always listed first when the function is called, 
            # second argument needs to be listed second when function is called and so on....

# Ex : 1

def person_name(first_name,second_name):
    print(first_name + second_name)
	
person_name("Ram","Babu")   # First name is Ram placed first
                            # Second name is Babu place second while calling a function.
                            
#-----------------------------------------------------------------------------------------------------------------------------

    #------------------#
    # Keyword Arguments:
    #------------------#
        
            # Keyword Arguments is an argument passed to a function or method which is preceded by a keyword and an equal to sign.
            # The order in keyword Arguments need not to be same as in positional argument.
            # while calling a function we explicitly telling python which argument value goes 
            # to which parameters in function declation by keyword names same as given in parameters.

# Ex : 1

def person_name(first_name,second_name):
    print(first_name + second_name)

person_name(second_name="Babu",first_name="Ram") # Here we are explicitly assigning the value. # order dosent matter

#---------------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------#
    # Positional Arguments & Keyword Arguments in same function:
    #----------------------------------------------------------#
        
            # if we specify positional arguments and  Keyword Arguments in same function its mandatory that 
            # we must specify "positional Arguments" "first" and then specify Keyword Arguments.
            # other wise we will get syntaxError.

# Ex : 1

def fruits(apple, banana, pineapple): # Non-default Parameters. # mandatory to pass 3 argument while calling this function.
    print('We have', apple+ ',', banana+ ' and', pineapple+ ' at our store.')

fruits("apple", "banana", "pineapple") # Positional Arguments. # order matters while calling function.

fruits(apple = 'apple', banana = 'banana', pineapple = 'pineapple') # Keyword Arguments # order doesn't matters while calling function.

fruits(banana = 'banana', pineapple = 'pineapple', apple = 'apple') # Keyword Arguments not in order 

fruits("apple", banana = "banana", pineapple = "pineapple")     # two Keyword Argument, one Positional Argument.
                                                                # Positional Arguments must be first.

# fruits(banana = 'banana', pineapple = 'pineapple', 'apple')# SyntaxError: positional argument follows keyword argument.

# fruits('apple', banana = 'banana', 'pineapple') # SyntaxError: positional argument follows keyword argument.

#------------------------------------------------------------------------------------------------------------------------------------------

    #------------------------------------------#
    # Python Default and Non-default Parameters:
    #------------------------------------------#

        #   Function parameters have default data assigned to them. (data can be callable function, string, int, float, boolean(True or False),complex )
        #   This can be done by using the assignment operator (=) in the function parameter. 
        #   When a function is called without an argument, the default data is used from parameter inside function. 
        #   This is useful when someone forgets to pass an argument while calling function and executes the program.
        #   default arguments(parameter) , must be followed by Non-default arguments(parameter).
        #   means we must write positional argument(parameter) first, then deafult argument(parameter)

        # Note – Python Default parameter are also called as Python Optional parameter.
        #        its not mandatory to pass default or optional parameter as an argument while calling a function.
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

    # o/p :
        # Values are:
        # 24
        # 10
        # 4

# Ex: 4

def adder(x,y,z):
    print("sum:",x+y+z)

adder(5,10,15,20,25)
# o/p: TypeError: adder() takes 3 positional arguments but 5 were given

#---------------------------------------------------------------------------------------------------------#
#===> To solve this problem (*args and **kwargs (Arbitrary Arguments) concept is impotant to learn) <=====#
#---------------------------------------------------------------------------------------------------------#

#----------------------------#
# Python Arbitrary Arguments :
#----------------------------#

#-------#
# *args :
#-------#

    # In this, we use the asterisk (*) to denote that perticular function only accept positional argument in function parameter. 
    # This is also called as Python *args. 
    # Python "*args" allows a function to "accept any number of positional arguments" passed while calling function
    # i.e. arguments which are non-keyword arguments, accepts variable-length(means no argument or less or more argument) while calling function.

    # Remember 'args' is just a notation. We can use any other parameter name instead of it.

# Ex: 1.0

# def adder(*args):   # accepts only positional arguments in the form of tuple
#     print("Tuple:",args)

# adder(a=5,b=10,c=15,d=20,e=25) # TypeError: adder() got an unexpected keyword argument 'a'

# Ex: 1.1
def adder(*args):   # accepts arguments in the form of tuple
    print("Tuple:",args) # o/p: Tuple: (5, 10, 15, 20, 25)
    print(type(args))   # o/p: <class 'tuple'>

adder(5,10,15,20,25) # calling adder with variable number of Arguments.   
    
# Ex: 1.2
def adder(*args): # args = (5,10,15,20,25) # packing using *  # accepts arguments in the form of tuple
    # a,b,c,d,e = *args # SyntaxError: can't use starred expression here(see unpacking concept)
    print("Unpacked data:",*args) # print is also a function  # so we can use unpacking operator * 

adder(5,10,15,20,25) # passed positional arguments while calling function.

# o/p : # o/p: Unpacked data: 5 10 15 20 25


# Ex: 1.3

def adder(*args): # args = (5,10,15,20,25) # packing using * # accepts arguments in the form of tuple
    a,b,c,d,e = args # Unpacking each data from tuple and assign it to respective variable(basic Unpacking in python)
    # a,b,c,d,e = *args # SyntaxError: can't use starred expression here
    # a, b, c, d = args # ValueError: too many values to unpack (expected 4) # values and variables must match
    # a, b, c, d, e, f = args # ValueError: not enough values to unpack (expected 6, got 5) # values and variables must match
    print("sum:",a+b+c+d+e)

adder(5,10,15,20,25) # o/p: 75


# Ex: 1.4

def my_sum_of_list(*args): # args = (10,20,30,40,50,60,70,80,90) # packing using *
    result = 0
    for x in args: # for x in (10,20,30,40,50,60,70,80,90) # iterating over each element in tuple
        result += x
    return result

list1 = [10, 20, 30]
list2 = [40, 50]
list3 = [60, 70, 80, 90]

print(my_sum_of_list(*list1, *list2, *list3)) # unpacking list data first using * operator then passed as arguments to function parameters.
# o/p: 450


#----------#
# **kwargs :
#----------#
        
        # In this, we use the asterisk (**) to denote that perticular function only accept Keyword argument in function parameter.
        #(see unpacking concept to understand ** operator)
        # Python "**kwargs" allows a function to "accept any number of Keyword arguments" passed while calling function
        # i.e. arguments which are keyword arguments, accepts variable-length(means no argument or less or more argument) while calling function.

    # arbitrary arguments come in handy when we don’t know how many arguments needed to pass in the function or method at that moment.

    # # Remember 'kwargs' is just a notation. We can use any other parameter name instead of it.

# Ex 1:

def concatenate(**words):   # words = {'language': 'python', 'version': '3.10.7', 'linking_verb': 'Is', 'appriciation': 'Great', 'e': '!'} 
                            # packs in dictionarie.
    print(words)
    print(type(words))
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(language="python", version="3.10.7", linking_verb="Is", appriciation="Great", e="!"))

    # o/p :
        # {'language': 'python', 'version': '3.10.7', 'linking_verb': 'Is', 'appriciation': 'Great', 'e': '!'}
        # <class 'dict'>
        # python3.10.7IsGreat!

# Ex : 2

def concatenate(**words): # words = {'language': 'python', 'version': '3.10.7', 'linking_verb': 'Is', 'appriciation': 'Great', 'e': '!'} # packs in dictionarie.
    print(words)
    print(type(words))
    
    valueresult = ""
    for value in words.values():
        valueresult += value
    

    keyresult = ""
    for key in words.keys():
        keyresult += key
        
    key_result = ""
    value_result = ""
    
    for key, value in words.items():
        key_result += key
        value_result += value
    
    key_value_string = key_result + value_result
    
    return valueresult, keyresult, key_value_string
valueresult, keyresult, key_value_string = concatenate(language="python", version="3.10.7", linking_verb="Is", appriciation="Great", e="!")
print(valueresult)
print(keyresult)
print(key_value_string)

    # o/p : 
        # {'language': 'python', 'version': '3.10.7', 'linking_verb': 'Is', 'appriciation': 'Great', 'e': '!'}
        # <class 'dict'>
        # python3.10.7IsGreat!
        # languageversionlinking_verbappriciatione
        # languageversionlinking_verbappriciationepython3.10.7IsGreat!
        
        
#-----------------------------------------------------#
# Standard arguments, *args, **kwargs in same function :
#-----------------------------------------------------#

            # the correct order for your parameters is:
                # Standard arguments
                # *args arguments
                # **kwargs arguments


# Ex : 0

def function(num,string="python 3.10.7",*args,**kwargs): 
    print(num)
    print(string)
    print(args)
    print(kwargs)

function(10) 

        # o/p : 
            # 10
            # python 3.10.7
            # ()
            # {}
        
    # Ex : 0.1
    
    # def function(num,string="python 3.10.7",*args,**kwargs): 
    #     print(num)
    #     print(string)
    #     print(args)
    #     print(kwargs)

    # function() # TypeError: function() missing 1 required positional argument: 'num'



# Ex : 1

def function1(*args,**kwargs): 
    print(args)
    print(kwargs)

function1(10, name = "mayur")

    # o/p : 
        # (10,)
        # {'name': 'mayur'}

    # Ex : 1.1
    # def function1(**kwargs, *args): # SyntaxError: invalid syntax
    #     print(args)
    #     print(kwargs)

    # function1(10, name = "mayur")



# Ex : 2

def function2(num, *args, **kwargs): 
    print(num)
    print(args)
    print(kwargs)

function2(10, "star args", 30, name = "mayur")
    # o/p : 
        # 10
        # ('star args', 30)
        # {'name': 'mayur'}

    # Ex : 2.1
    # def function(*args, **kwargs, num): # SyntaxError: invalid syntax
    #     print(num)
    #     print(args)
    #     print(kwargs)

    # function("star args", 30, name = "mayur",10)



# Ex : 3

def function3(num, *args, sirname = "Adhude", **kwargs): 
    print(num)
    print(sirname)
    print(args)
    print(kwargs)

function3(10, "star args", 30, name = "mayur")

    # o/p : 
        # 10
        # Adhude
        # ('star args', 30)
        # {'name': 'mayur'}
        
        # Ex : 3.1
        # def function3(num, sirname = "Adhude", *args, **kwargs): 
        #     print(num)
        #     print(args)
        #     print(sirname)
        #     print(kwargs)

        # function3(10, "star args", 30, sirname = "bhosle", name = "mayur") # TypeError: function3() got multiple values for argument 'sirname'
        
        
        # Ex : 3.2
        # def function(num, *args, sirname = "Adhude", **kwargs): 
        #     print(num)
        #     print(args)
        #     print(sirname)
        #     print(kwargs)

        # function(10, sirname = "bhosle", "star args", 30, name = "mayur") # SyntaxError: positional argument follows keyword argument



# Ex : 4

def function(num, name = "mayur", *args, **kwargs): 
    print(num)
    print(name)
    print(args)
    print(kwargs)

function(10, (1,5,8,9), sirname = "Adhude" )

    # o/p : 
        # 10
        # (1, 5, 8, 9)
        # ()
        # {'sirname': 'Adhude'}
#-------------------------------------------------------------------------------------------#

#----------------------------------------------------------------#
# (PEP 570) Positional-Only Parameters & Keyword-Only parameters #
#----------------------------------------------------------------#

    # This PEP(Python Enhancement Proposal) 570 proposes to introduce a new syntax, /(forward-slash), 
    # and * for specifying positional-only parameters and Keyword-Only parameters recpectively in Python function definitions.


#----------------------------#
# Positional-Only Parameters #
#----------------------------#

        # Positional-only parameters would be placed before a / (forward-slash).
        # The / is used to logically separate the positional-only parameters from the rest of the parameters.
        # If there is no / in the function definition, there are no positional-only parameters.
        
        # Parameters after the / may be positional-or-keyword or keyword-only.

def standard_arg(arg):
    print(arg)
    
standard_arg(2)
standard_arg(arg=2)
    # o/p : 2
    #       2

def pos_only_arg(arg, /):
    print(arg)
    
pos_only_arg(1)
pos_only_arg(arg=1)
# o/p : 1
#       TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

def pos_only_arg(pos1, /, pos2, kw_arg, kw_r, optl_kw = 7): # Parameters after the / may be positional-or-keyword or keyword-only and at last optional keyword parameter.
    print(pos1)
    print(pos2)
    print(kw_arg)
    print(kw_r)
    print(optl_kw)
    
pos_only_arg(3,"mayur", kw_arg = 3, kw_r=2, optl_kw = 8)


#-------------------------#
# Keyword-Only Parameters #
#-------------------------#

        # To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument,
        # place an only * in the arguments list just before the first keyword-only parameter.
        
        # Parameters before the * may be Positional-Only or positional-or-keyword


def kwd_only_arg(*, arg): # function kwd_only_args only allows keyword arguments while calling as indicated by a * in the function definition
    print(arg)

kwd_only_arg(arg=3)
kwd_only_arg(3) # TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given


def kwd_only_arg(pos, kw, *, kw_arg, kw_r):  # Parameters before the * may be Positional-Only or positional-or-keyword
    print(pos)
    print(kw)
    print(kw_arg)
    print(kw_r)
    
kwd_only_arg(3, kw = 8, kw_arg = 3, kw_r=2)
    # o/p :
        # 3
        # 8
        # 3
        # 2


#-------------#
# Combination #
#-------------#


        # def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        #       -----------    ----------     ----------
        #         |             |                  |
        #         |        Positional or keyword   |
        #         |                                |
        #         |                                |--> Keyword only
        #         |--> Positional only


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, kwd_only=3) # o/p : 1 2 3
combined_example(1, standard=2, kwd_only=3) # o/p : 1 2 3
combined_example(1, 2, 3) # TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

#----------------------------------#
# issue solved with above apporach #
#----------------------------------#


# def func5(name, name = 5): # SyntaxError: duplicate argument 'name' in function definition
#     print(name)

# name = func5(1, **{'name': 2}) # # func5(1, **{'name': 2}) is same as func5(1, name = 2) # unpacking {'name' : 2} with **.
# print(name)


        #issue
def func5(name, **kwds):    # valid definition but there is a issue(name getting multiple values 1 and 2)
                            #(while calling we are providing Multiple values to name parameter,
                            # name already got 1 and again we are providing name = 2 i.e 2 value to name)
                            # this sometimes happens because data(i.e key) in dictionarie having same name as function parameter Name
                            # func5(1, **{'name': 2}) is same as func5(1, name = 2) # unpacking {'name' : 2} with **.
    return 'name' in kwds

func5(1, **{'name': 2}) # TypeError: func5() got multiple values for argument 'name'

        # we can solve this problem, telling python to take positional-only argument to left side of /(forword-slash)

def func5(name, /, **kwds):
    return 'name' in kwds

name = func5(1, **{'name': 2})  # func5(1, **{'name': 2}) is same as func5(1, name = 2) # unpacking {'name' : 2} with **.
                                # while unpacking dictionarie with ** we get keyword argument(key as argument Name and assinging associate vale to it)
print(name) # o/p : True