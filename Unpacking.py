#--------------------------------#
# Unpacking and Packing in Python:
#--------------------------------#
        
        # Unpacking in Python refers to an operation that consists of assigning an iterable of values to a left hand side
        # (tuple) or [list] of variables in a single assignment statement.
        
        # When it comes to unpacking in Python, we can use any iterable on the right side of the assignment "=" operator.
        # The left side can be filled with a (tuple) or with a [list] of variables.
        
        # Ex : 0.0
            # (a, b, c) = 1, 2, 3
            # print("a:",a,"b:",b,"c:",c) # o/p: a: 1 b: 2 c: 3
            # print(type(a),type(b),type(c)) # o/p: <class 'int'> <class 'int'> <class 'int'>
        
        # Ex : 0.1
            # [a, b, c] = 1, 2, 3
            # print("a:",a,"b:",b,"c:",c) # o/p: a: 1 b: 2 c: 3
            # print(type(a),type(b),type(c) # o/p: <class 'int'> <class 'int'> <class 'int'>
        
        # It works the same way if we use the range() iterator:
        # x, y, z = range(3)
        # print(x,y,z) # o/p: 0 1 2
        
        # operation that consists of assigning an iterable of values of right hand side to a left hand side
        
        # {set} or dict {key:values} of variables in a single assignment statement is not allowed.
        # Ex : 0.0
            # {a,b,c} = 1,2,3 # SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
            # print("a:",a,"b:",b,"c:",c)
        
        # Ex : 0.1
            # {a : 4 , b : 5, c : 6} = 1,2,3 # SyntaxError: cannot assign to dict literal here. Maybe you meant '==' instead of '='?
            # print("a:",a,"b:",b,"c:",c)

#-------------------------------------------------------------------------------------------------------------------------------------#        

#--------------------#
# iterable unpacking :
#--------------------#

        # Any iterable in python, a list(ordered), dict(ordered), tuple(ordered), set(unordered) is said to have a pack of values.(String is also iterable object)
        # We can unpack the values from an iterable into a individual variables.
        
        # As of Python version 3.10.7, dictionaries are "ordered". In Python 3.6 and earlier, dictionaries are unordered.
        # Note: in case of unordered iterables like a set(duplicate elements not considered), the sequence of values unpacked into different variables is not guaranteed.
        # Once a set is created, you cannot change its items, but you can remove items and add new items.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------#
# Unpacking Tuples(ordered) :
#---------------------------# 
    # In Python, we can put a tuple of variables on the left side of an assignment operator (=) and 
    # a tuple of values on the right side.
    
    # The values on the right will be automatically assigned to the variables on the left according to their position in the tuple.

# Ex : 1.0

(a, b, c) = (1, 2, 3)
print("a:",a,"b:",b,"c:",c) # o/p : a: 1 b: 2 c: 3
    # When we put tuples on both sides of an assignment operator, a tuple unpacking operation takes place. 
    # The values on the right are assigned to the variables on the left according to their relative position in each tuple.
    
    # To create a tuple object, we don't need to use a pair of parentheses () as delimiters.
    # This also works for tuple unpacking, so the following syntaxes are equivalent:

# Ex : 1.1

(a, b, c) = 1, 2, 3 # syntax 1
print("a:",a,"b:",b,"c:",c) # o/p: a: 1 b: 2 c: 3
a, b, c = (1, 2, 3) # syntax 2
print("a:",a,"b:",b,"c:",c) # o/p: a: 1 b: 2 c: 3
a, b, c = 1, 2, 3   # syntax 3
print("a:",a,"b:",b,"c:",c) # o/p: a: 1 b: 2 c: 3

    # Arguably, the last syntax is more commonly used when it comes to unpacking in Python.
    
    # When we are unpacking values into variables using tuple unpacking,
    # the number of variables on the left side tuple must exactly match the number of values on the right side tuple.
    # Otherwise, we'll get a ValueError.

# Ex : 1.2

a, b = 1, 2, 3 # ValueError: too many values to unpack (expected 2)
print("a:",a,"b:",b)

    # Note: The only exception to this is when we use the * operator to pack several values in one variable as we'll see later on.
    
    # On the other hand, if we use more variables than values,
    # then we'll get a ValueError but this time the message says that there are not enough values to unpack:

# Ex : 1.3

a, b, c = 1, 2 # ValueError: not enough values to unpack (expected 3, got 2)
print("a:",a,"b:",b,"c:",c)

# Ex : 1.4

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

# Ex : 1.5

x = (1,2,"a",8,{ "key" : 2, "value" : 3 },9) # dictionarie in tuple.
a, b, c, d, e, f = x
print("a==>",a,"b==>",b,"c==>",c,"d==>",d,"e==>",e,"f==>",f) 
    # o/p: a==> 1 b==> 2 c==> a d==> 8 e==> {'key': 2, 'value': 3} f==> 9

#-----------------------------------------------------------------------------------------------------#

#-------------------------#
# Unpacking List(ordered) :
#-------------------------#

# Ex : 1

a, b, c, d = [1, '2', {1,2}, 2.3] # list
print(a,b,c,d) # o/p: 1 2 {1, 2} 2.3


#-----------------------------------------------------------------------------------------------------#

#--------------------------------#
# Unpacking dictionarie(ordered) :
#--------------------------------#

    # duplicate keys will be discarded(if duplicate keys is available while program runs, number of elements in dict will reduce so while unpacking at runtime will give error )
    # while basic unpacking dictionaries {key : values} only "keys" will be unpacked to corresponding variable from left to right

# Ex : 1.1

a,b = {'mayur': 29, 'priyanka': 29} # unpacking only key
print(a)
print(b)
# o/p:
    # mayur
    # priyanka

# Ex : 1.2

a = {
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    } # if duplicate keys exists in dictionarie only last key is considered all the keys before last one will be discarded.
print(a) # o/p : {'mayur': 100, 'priyanka': 29}

# Ex : 1.3

# if duplicate keys is available while program is in running state, number of elements in dict will reduce so while unpacking at runtime will give error.
a,b,c = {
    'mayur': 29,
    'priyanka': 29,
    'mayur': 29,
    } # ValueError: not enough values to unpack (expected 3, got 2)
print(a,b,c)

# Ex : 1.4
    # Unpacking dictionaries (keys, values, and items)

my_dict = {'one': 1, 'two':2, 'three': 3}

a, b, c = my_dict # Unpack keys
print(type(a),":",a,":",type(b),b,":",type(c),c) # o/p: <class 'str'> : one <class 'str'> : two <class 'str'> : three

a, b, c = my_dict.values() # Unpack values
print(type(a),":",a,":",type(b),b,":",type(c),c) # o/p: <class 'int'> : 1 <class 'int'> : 2 <class 'int'> : 3

a, b, c = my_dict.items() # Unpacking key-value pairs
print(type(a),":",a,":",type(b),b,":",type(c),c) # o/p: <class 'tuple'> : ('one', 1) <class 'tuple'> : ('two', 2) <class 'tuple'> : ('three', 3)


#----------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------#
# Unpacking Set(ordered) :
#------------------------#

    # in case of unordered iterables like a set(duplicate elements not considered), 
    # the sequence of values unpacked into different variables is not guaranteed.

# Ex : 1.1

v,o,w,e,l = {'a', 'e', 'i', 'o', 'u'} # set
print("v : ",v, ", o : ",o, ", w : ",w,", e : ",e,", l : ",l) # o/p: v :  u , o :  e , w :  a , e :  o , l :  i

# Ex : 1.2

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
        
#----------------------------------------------------------------------------------------------------------------#

#----------------------#
# Unpacking generators :
#----------------------#

gen = (2 ** x for x in range(3))
print(gen)  # o/p : <generator object <genexpr> at 0x0000029804C242E0>
print(type(gen)) # o/p: <class 'generator'>
a, b, c = gen # Unpacking generators
print(a,b,c) # o/p: 1 2 4
print(type(a),type(b),type(c)) # o/p: <class 'int'> <class 'int'> <class 'int'>

#----------------------------------------------------------------------------------------------------------------#

                            #----------------------------------#
                            # Unpacking Operators ( * and ** ) #
                            #----------------------------------#

        # unpacking operators are operators that unpack the values from iterable(lists,tuples and strings) objects in Python.

#---------------------------------------#        
# Unpacking Operator * (asterisk / star)#
#---------------------------------------#

        # The single asterisk operator * can be used on any iterable(lists,tuples and strings) object that Python provides.


#-----------#
# * on List :
#-----------#

# Ex : 1.0

my_list = [1, 2, 3]
print(my_list) # o/p : [1, 2, 3]

        # Note how the list is printed, along with the corresponding brackets and commas.
        
        # Now, try to prepend the unpacking operator * to the name of your list:

my_list = [1, 2, 3]
print(*my_list) # o/p: 1 2 3

        # Instead of a list, print() has taken three separate arguments as the input.
        # you used the unpacking operator * in function call , instead of in a function definition.
        # In this case, print() takes all the items of a list as though they were single arguments.
        # You can also use this method to call your own functions, 
        # but if your function requires a specific number of parameter, 
        # then the iterable you unpack must have the same number of arguments in function call.

# Ex : 2

def my_sum(a, b, c): #  a, b, and c are required parameter.
    print(a + b + c)

my_list = [1, 2, 3, 4]
my_sum(*my_list)    # 1 2 3 4 # * operator unpack 4 items from the list. 
                    # o/p: TypeError: my_sum() takes 3 positional arguments but 4 were given

# Ex : 5

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list) # o/p :[1, 2, 3, 4, 5, 6]



#-----------------------------#
# Packing With the * Operator :
#-----------------------------#

        # The * operator is known, in this context, as the tuple (or iterable) unpacking operator.
        # It extends the unpacking functionality to allow us to collect or pack multiple values in a single variable.
        

        # Converting variable-length iterable in single variable into a list # tricky concept
# Ex : 1

        # When you use the unpacking operator with single variable assignment, 
        # Python requires that your resulting variable is either a list or a tuple.

        # *a = "RealPython"
        # print(a) # SyntaxError: starred assignment target must be in a list or tuple

        # if you want to unpack all items of the variable-length iterable into a single variable, a, 
        # then you need to add the comma (,) without naming a second variable.
        # Python will then unpack all items into the first named variable, which is a list.
        # here we have to use tuple unpacking in combination with the unpacking operator *.

*a, = "RealPython"  # There’s the unpacking operator *, followed by a variable, and comma, and an assignment.
print(a)    # o/p : ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

        # The comma after the "a" does the trick.
        # With the trailing comma, you have defined a tuple with only one named variable, a, which is the list
        # Where is the tuple ????
            # You never get to see the tuple that Python creates in this operation,
            # because you use tuple unpacking in combination with the unpacking operator *.
# Ex : 2
        # If you name a second variable on the left-hand side of the assignment, 
        # Python will assign the last character of the string to the second variable, 
        # while collecting all remaining characters in the list a

*a, b = "RealPython"
print(a, type(a))
print(b, type(b))
    # o/p:
        # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o'] <class 'list'>
        # n <class 'str'>

# Ex : 3

    # if we need to split a list into three different parts.
    # The output should show the first value, the last value, and all the values in between.
    # With the unpacking operator, you can do this in just one line of code:

my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list  # The first data from list is assigned to a, the last data to c, 
                    # and all other values are "packed" into a new list b

print(a)
print(b)
print(c)
    # o/p:
        # 1
        # [2, 3, 4, 5]
        # 6

# Ex : 4

my_list = [1, 2, 3, 4, 5, 6]
a, b, *c = my_list  #  The first data from list is assigned to a, the second data to b, 
                    # and all other values are "packed" into a new list c
print(a)
print(b)
print(c)
    # o/p: 
        # 1
        # 2
        # [3, 4, 5, 6]

# Ex : 6

*a, = {     # Converting variable-length iterable in single variable a of list type.
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }
print(a, type(a)) # o/p: ['mayur', 'priyanka'] <class 'list'>

# print(a.items())	# AttributeError: 'list' object has no attribute 'items'

# Ex : 7

*a,b = {    # Converting variable-length iterable in single variable a of list type.
            # Python will assign the last character of the string type to the second variable b and 
            # reamining packed into "a" of list type. 
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }
print(a, type(a))   # o/p: ['mayur'] <class 'list'>
print(b, type(b))   # o/p: priyanka <class 'str'>

# print(a.items())	# o/p: AttributeError: 'list' object has no attribute 'items'
# print(b.items())	# AttributeError: 'str' object has no attribute 'items'

# Ex : 8

    # *a,*b = {     # multiple starred expressions in assignment is not allowed
    #     '2': 200,
    #     '2': 9,
    #     2: 100,
    #     1: 29,
    #     } 
    # print(type(a),type(b))
    # print(a,b)
    # o/p: SyntaxError: multiple starred expressions in assignment


# Ex : 9

*a, = (1,2,"a",8,{ "key1" : 2, "key2" : 3 },9) # Converting variable-length iterable in single variable a of list type.
print(a, type(a)) # o/p: [1, 2, 'a', 8, {'key': 2, 'value': 3}, 9] <class 'list'>

# a.items() # o/p: AttributeError: 'list' object has no attribute 'items'

key1, key2 = a[4]	# Unpack keys
print(key1,key2)    # o/p: key1 key2

value1, value2 = a[4].values() # Unpack values
print(value1,value2) # o/p: 2 3

key1_value1, key2_value2 = a[4].items()	# Unpacking key-value pairs (by default in tuple)
print(key1_value1,key2_value2)  # o/p: ('key1', 2) ('key2', 3)

x, y = key1_value1
print(x,y) # o/p: key1 2
w, z = key2_value2
print(w,z) # o/p: key2 3


# Ex : 10

*a,b = (1,2,"a",8,9,
        {   
            "key1" : 2, 
            "key2" : 3 
        }
        )  # Converting variable-length iterable in single variable a of list type.
            # Python will assign the last character of the dict type to the second variable b, because b is mandatory

print(a, type(a))   # o/p: [1, 2, 'a', 8, 9] <class 'list'>
print(b, type(b)) 	# o/p: {'key1': 2, 'key2': 3} <class 'dict'>

key1, key2 = b  # Unpack keys
print(key1,key2) # o/p: key1 key2

value1, value2 = b.values() # Unpack values
print(value1,value2) # o/p: 2 3

key1_value1, key2_value2= b.items() # Unpacking key-value pairs
print(key1_value1, key2_value2) # o/p: ('key1', 2) ('key2', 3)

# Ex : 11

*a,b = (1,2,"a",8,9,
        {   
            "key1" : 2, 
            "key2" : 3 
        }
        )  # Converting variable-length iterable in single variable a of list type.
            # Python will assign the last character of the dict type to the second variable b, because b is mandatory

print(a, type(a))   # o/p: [1, 2, 'a', 8, 9] <class 'list'>
print(b, type(b)) 	# o/p: {'key1': 2, 'key2': 3} <class 'dict'>

key1_value1, key2_value2 = b.items()    # Unpacking key-value pairs in tuple
print(key1_value1, key2_value2) # o/p: ('key1', 2) ('key2', 3)

key1, value1 = key1_value1  # unpacking data key and value from tuple
key2, value2 = key2_value2  # unpacking data key and value from tuple
print(key1,key2) # o/p: key1 key2
print(value1,value2) # o/p: 2 3


# Ex : 12

*a, b, c, d = 1, 2, 3 # Packing no values in a (a defaults to empty []) because b, c, and d are mandatory
print(a, b, c, d) # o/p: [] 1 2 3

#------------------------------------------------------------------------------------------------------------------