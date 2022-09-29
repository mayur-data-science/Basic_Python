# Python Arguments :

# Parameters: 
        # A parameter is the variable defined within the parentheses during function definition. 
        # Simply they are written when we declare a function. 

# Ex 1

def sum(a,b): # Here a,b are the parameters
    print(a+b)
    
sum(1,2)

# Arguments:
        # An argument is a value that is passed to a function when it is called. 
        # It might be a variable, value or object passed to a function or method as input. 
        # They are written when we are calling the function.

# Ex1:

def sum(a,b):
    print(a+b)
    
sum(1,2) # Here the values 1,2 are arguments

# Positional Arguments :
        # Positional Arguments are needed to be included in proper order
        # i.e the first argument is always listed first when the function is called, 
        # second argument needs to be listed second when function is called and so on....
        
# Ex 1
def person_name(first_name,second_name):
    print(first_name + second_name)
	
person_name("Ram","Babu")   # First name is Ram placed first
                            # Second name is Babu place second while calling a function.

# Keyword Arguments:
        # Keyword Arguments is an argument passed to a function or method which is preceded by a keyword and an equal to sign.
        # The order in keyword Arguments need not to be same as in positional argument.
        # while calling a function we explicitly telling python which argument value goes to which parameters in function declation by keyword names same as given in parameters.
# Ex1

def person_name(first_name,second_name):
    print(first_name + second_name)

person_name(second_name="Babu",first_name="Ram") # Here we are explicitly assigning the value. # order dosent matter

# Positional Arguments & Keyword Arguments in same function:
        # if we specify positional argument and  Keyword Arguments in same function its mandatory that 
        # we must specify "positional Arguments" "first" and then specify Keyword Arguments.
        # other wise we will get syntaxError.

def fruits(a, b, p): # Non-default Parameters. # mandatory to pass 3 argument while calling this function.
    print('We have', a+ ',', b+ ' and', p+ ' at our store.')

fruits('apple', 'banana', 'pineapple') # Positional Arguments. # order matters while calling.

fruits(a = 'apple', b = 'banana', p = 'pineapple') # Keyword Arguments # order doesn't matters while calling.

fruits(b = 'banana', p = 'pineapple', a = 'apple') # Keyword Arguments not in order 

fruits('apple', b = 'banana', p = 'pineapple')  # two Keyword Argument, one Positional Argument.
                                                # Positional Arguments must be first.

# fruits(b = 'banana', p = 'pineapple', 'apple')# SyntaxError: positional argument follows keyword argument.
# fruits('apple', b = 'banana', 'pineapple') # SyntaxError: positional argument follows keyword argument.



# Python Default Arguments:
    #   Function parameters have default data assigned to them. (data can be callable function, string, int, float, boolean(True or False) )
    #   This can be done by using the assignment operator (=) in the function parameter. 
    #   When a function is called without  an argument, the default data is used from parameter. 
    #   This is useful when someone forgets to pass an argument to the function and executes the program.
    #   default arguments , must be followed by Non-default arguments(positional argument).
    #   means we must write positional argument first, then deafult argument

    # Note – Python Default arguments are also called as Python Optional arguments.
    #        its not mandatory to pass default or optional argument while calling a function.
    #        if we provide default argument while calling function, the dafault data will not be utilized from function parameter.(overridding deafult data)
    #        if we dont provide default argument while calling function, the default data will be utilized from function parameter.

# Ex1: 
def welcome(fullname, msg = 'Welcome to python!!'): # fullname is positional parameter and msg is default parameter.
    print('Hey there', fullname + ', ' + msg) # If the msg argument is not provided while calling function, then the default data from the function parameter is utilized.

welcome('Sam')  # Here we are only passing one positional argument which is mandatory. 
                # and we are not passing second argument which is "optional argument" while calling function
                # while calling a function its mandatory to pass argument in same order which defined in function declaration as parameter.
welcome('Zack', 'How have you been?') # 2nd argument value(data) passed; will not use functions default parameter data.

# o/p: 
    # Hey there Sam, Welcome to python!!
    # Hey there Zack, How have you been?


# Ex 2: default parameter having callable function.
def add_str():
    return "You Are Awesome"

def welcome(fullname, msg = add_str): # fullname is positional parameter and msg is default parameter which is callable function.
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


# Ex 2
    # Non-default arguments, cannot be followed by default arguments.

def function(a = 24, b, c):
    print('Values are:')
    print(a)
    print(b)
    print(c)

function(10, 4)

# o/p: SyntaxError: non-default argument follows default argument





# Python Arbitrary Arguments :
# In this, we use the asterisk (*) to denote this method before the parameter in the function. 
# This is also called as Python *args. 
# Python *args allows a function to accept any number of positional arguments 
# i.e. arguments which are non-keyword arguments, variable-length argument list.

# Remember 'args' is just a notation. We can use any other argument name instead of it.

# arbitrary arguments come in handy when we don’t know how many arguments are needed in the program at that moment.