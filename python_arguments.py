### Python Arguments :

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

### Iterable Unpacking: 
        # Any iterable in python, a list(ordered), dict(ordered), tuple(ordered), set(unordered) is said to have a pack of values.(String is also iterable object)
        # We can unpack the values from an iterable into a individual variables.
        
        # As of Python version 3.10.7, dictionaries are "ordered". In Python 3.6 and earlier, dictionaries are unordered.
        # Note: in case of unordered iterables like a set(duplicate elements not considered), the sequence of values unpacked into different variables is not guaranteed.
        # Once a set is created, you cannot change its items, but you can remove items and add new items.
#------------------------------------------------------------------------------------------------------------
# Ex : 1.0 list
a, b, c, d = [1, '2', {1,2}, 2.3] # list
print(a,b,c,d) # o/p: 1 2 {1, 2} 2.3

#--------------------------------------------------------------------------------------------------------------
# Ex : 1.0 # accessing each character of string
a = "mayur"
print(a[0],a[1],a[2],a[3],a[4])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# o/p: 
    # m a y u r
    # a
    # y
    # u
    # r

# Ex : 1.1 String
    # We can also unpack an iterable which is stored in a variable.
from collections.abc import Iterable
v = 'python' # string
a, b, c, d, e, f = v
print(a,b,c,d,e,f) # o/p: p y t h o n
if isinstance(v, Iterable):
    print(f"{v} String is iterable")  
else:
    print(f"{v} Int is not iterable")
# o/p:  
    # p y t h o n
    # python String is iterable
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Ex : 1.2 # set
# in case of unordered iterables like a set(duplicate elements not considered), the sequence of values unpacked into different variables is not guaranteed.
v,o,w,e,l = {'a', 'e', 'i', 'o', 'u'} # set
print("v : ",v, ", o : ",o, ", w : ",w,", e : ",e,", l : ",l) # o/p: v :  u , o :  e , w :  a , e :  o , l :  i

# Ex : 1.3
x = {100,500,'s',50} # set
a,b,c,d = x
print("a:",a,"b:",b,"c:",c,"d:",d) # o/p: a: 50 b: s c: 100 d: 500

# Ex : 1.4
x = {100,170,180,160,210} # set
a,b,c,d,e = x
print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e) # o/p: a: 160 b: 210 c: 100 d: 180 e: 170

# Ex : 1.5
x = {100,170,180,160,100} # set with duplicate element (100).
print(x) # o/p: {160, 100, 170, 180} # only considered one value other one discarded
a,b,c,d,e = x
print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e) 
# o/p:
    # {160, 100, 170, 180}
    # ValueError: not enough values to unpack (expected 5, got 4)

# Ex : 1.6
x = {100,170,180,160,100} # set
print(x)
a,b,c,d = x
print("a:",a,"b:",b,"c:",c,"d:",d)
if hasattr(x, '__iter__'):
    print(f'set {x} is iterable')
else:
    print(f'{x} is not iterable')
# o/p: 
    # {160, 100, 170, 180}
    # a: 160 b: 100 c: 170 d: 180
    # set {160, 100, 170, 180} is iterable
#--------------------------------------------------------------------------------------------------------------
# Ex : 1.7 # tuple
# x = (1, 1, 2, 3, 5)   # Parentheses are optional
                        # but always use Parentheses as a standard practice to avoid ambiguity
x = 1, 1, 2, 3, 5
print(x, type(x))
a,b,c,d,e = x # Unpacking tuple
print(a,b,c,d,e)
print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e)
# o/p:
    # (1, 1, 2, 3, 5) <class 'tuple'>
    # 1 1 2 3 5
    # a: 1 b: 1 c: 2 d: 3 e: 5
# Ex : 1.7.1
x = (1,2,"a",8,{ "key" : 2, "value" : 3 },9) # dictionarie in tuple.
a, b, c, d, e, f = x
print("a==>",a,"b==>",b,"c==>",c,"d==>",d,"e==>",e,"f==>",f) # o/p: a==> 1 b==> 2 c==> a d==> 8 e==> {'key': 2, 'value': 3} f==> 9

#------------------------------------------------------------------------------------------------------------
# Ex : 1.8 Dictionaries(ordered)
# duplicate keys will be discarded(if duplicate keys is available while program runs, number of elements in dict will reduce so while unpacking at runtime will give error )
# while basic unpacking dictionaries {key : values} only "keys" will be unpacked to corresponding variable from left to right
# Ex : 1.8.1
a,b = {'mayur': 29, 'priyanka': 29}
print(a)
print(b)
# o/p:
    # mayur
    # priyanka

# Ex : 1.8.2
a = {
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    } # if duplicate keys exists in dictionarie only last key is considered all the keys before last one will be discarded.
print(a) # o/p : {'mayur': 100, 'priyanka': 29}}

# Ex : 1.8.3
# if duplicate keys is available while program is in runing state, number of elements in dict will reduce so while unpacking at runtime will give error.
a,b,c = {
    'mayur': 29,
    'priyanka': 29,
    'mayur': 29,
    } # ValueError: not enough values to unpack (expected 3, got 2)
print(a,b,c)

#---------------------------------------------------------------------------------------------------------------------------

# Unpacking Operators ( * and ** ) :
    # unpacking operators are operators that unpack the values from iterable objects in Python.
#---------------------------------------------------------------------------------------------------------------------------    
# * (asterisk / star): 
        # The single asterisk operator * can be used on any iterable(lists,tuples and strings) object that Python provides.

# Ex : 1.0       
my_list = [1, 2, 3]
print(my_list)
        
# o/p : [1, 2, 3]
        # Note how the list is printed, along with the corresponding brackets and commas.
        
        # Now, try to prepend the unpacking operator * to the name of your list:
        
my_list = [1, 2, 3]
print(*my_list)
        
# o/p: 1 2 3
        # Instead of a list, print() has taken three separate arguments as the input.
        # you used the unpacking operator * in function call , instead of in a function definition.
        # In this case, print() takes all the items of a list as though they were single arguments.
        # You can also use this method to call your own functions, 
        # but if your function requires a specific number of parameter, 
        # then the iterable you unpack must have the same number of arguments in function call.

def my_sum(a, b, c): #  a, b, and c are required parameter.
    print(a + b + c)

my_list = [1, 2, 3, 4]
my_sum(*my_list) # 1 2 3 4 # * operator unpack 4 items from the list. 

# o/p: TypeError: my_sum() takes 3 positional arguments but 4 were given

# if we need to split a list into three different parts.
# The output should show the first value, the last value, and all the values in between.
# With the unpacking operator, you can do this in just one line of code:

# Ex : 1.1        
my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list #  The first data from list is assigned to a, the last data to c, and all other values are packed into a new list b
print(a)
print(b)
print(c)
# o/p:
    # 1
    # [2, 3, 4, 5]
    # 6

# Ex : 1.2
my_list = [1, 2, 3, 4, 5, 6]
a, b, *c = my_list #  The first data from list is assigned to a, the second data to b, and all other values are packed into a new list c
print(a)
print(b)
print(c)
# o/p: 
    # 1
    # 2
    # [3, 4, 5, 6]

# Ex : 1.3 
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

# o/p :[1, 2, 3, 4, 5, 6]

# Ex : 1.0
x = (1,2,1,8,7,9) # Tuple
print(x) # o/p : (1, 2, 1, 8, 7, 9)
print(*x) # o/p: 1 2 1 8 7 9

# Ex : 1.1
x = (1,2,"a",8,{ "key" : 2, "value" : 3 },9) # dictionarie in tuple
print(x) # o/p : (1, 2, 'a', 8, {'key': 2, 'value': 3}, 9)
print(*x) # o/p : 1 2 a 8 {'key': 2, 'value': 3} 9


a = [*"mayur"] # * operator works on any iterable object. It can also be used to unpack a string:
print(a) # o/p : ['m', 'a', 'y', 'u', 'r']

a = "mayur"
print(*a) # o/p : m a y u r

# a = *"mayur" # SyntaxError: can't use starred expression here
# print(a)

# Ex : 2
a = {
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    } # if duplicate keys exists in dictionarie only last key is considered all the keys before last one will be discarded.
print(*a) # unpacking dictionarie with * , only keys will be unpacked.
# o/p: mayur priyanka

a = {
        "nested1": {
            "mayur": 100,
            'priyanka': 29,
        },
        
        "nested2": {
            "mayur": 100,
            'priyanka': 29,
        }
    }

print(*a) # o/p : nested1 nested2

a1 = {1 : "a", 2 : "b"}
a2 = {3 : "c", 4 : "d"}
a3 = {5 : "e", 6 : "f"}

d1 = {*a1,*a2,*a3}
print(d1) # o/p :{1, 2, 3, 4, 5, 6}

#------------------------------------------------------------------------------------------------------------

### Converting variable-length iterable in single variable into a list # tricky concept
# Ex : 1

# When you use the unpacking operator with single variable assignment, Python requires that your resulting variable is either a list or a tuple.

# *a = "RealPython"
# print(a) # SyntaxError: starred assignment target must be in a list or tuple

# if you want to unpack all items of the variable-length iterable into a single variable, a, then you need to add the comma (,) without naming a second variable.
# Python will then unpack all items into the first named variable, which is a list.
# here we have to use tuple unpacking in combination with the unpacking operator *.

*a, = "RealPython" # There’s the unpacking operator *, followed by a variable, and comma, and an assignment.
print(a) # o/p : ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

# The comma after the "a" does the trick.
# With the trailing comma, you have defined a tuple with only one named variable, a, which is the list
# Where is the tuple ????
    # You never get to see the tuple that Python creates in this operation, because you use tuple unpacking in combination with the unpacking operator *.

# If you name a second variable on the left-hand side of the assignment, 
# Python will assign the last character of the string to the second variable, 
# while collecting all remaining characters in the list a

*a, b = "RealPython"
print(a, type(a))
print(b, type(b))
# o/p:
    # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o'] <class 'list'>
    # n <class 'str'>
            
            #----------------------------------------------------#

# Ex : 2
*a, = {
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }
print(a, type(a)) # o/p: ['mayur', 'priyanka'] <class 'list'>

*a,b = {
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }
print(a, type(a))
print(b, type(b))
# o/p: 
    # ['mayur'] <class 'list'>
    # priyanka <class 'str'>

# *a,*b = {
#     '2': 200,
#     '2': 9,
#     2: 100,
#     1: 29,
#     } 
# print(type(a),type(b))
# print(a,b)
# o/p: SyntaxError: multiple starred expressions in assignment
            
            #----------------------------------------------------#

# Ex : 3
*a, = (1,2,"a",8,{ "key" : 2, "value" : 3 },9)
print(a, type(a)) # o/p: [1, 2, 'a', 8, {'key': 2, 'value': 3}, 9] <class 'list'>

*a,b = (1,2,"a",8,{ "key" : 2, "value" : 3 },9)
print(a, type(a))
print(b, type(b))
# o/p:
    # [1, 2, 'a', 8, {'key': 2, 'value': 3}] <class 'list'>
    # 9 <class 'int'>


#-------------------------------------------------------------------------------------



### ** (double  asterisk / double star) :
        #  the double asterisk operator ** can only be used on "dictionaries".
        # ** unpacking operator unpack key and values also.

# Ex : 1.0
x = (1,2,1,8,7,9) # Tuple
print(**x) # o/p : TypeError: print() argument after ** must be a mapping, not tuple

# Ex : 2.0
a1 = {1 : "a", 2 : "b"}
print(a1)
# Ex : 2.1
a1 = {1 : "a", 2 : "b"}
a2 = {3 : "c", 4 : "d"}
a3 = {5 : "e", 6 : "f"}

d2 = {**a1,**a2,**a3}
print(d2) # o/p : {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}



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


