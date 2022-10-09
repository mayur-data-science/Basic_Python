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

#-------------------------------------#
# Unpacking Tuples(ordered-immutable) :
#-------------------------------------# 
    # In Python, we can put a tuple of variables on the left side of an assignment operator (=) and 
    # a tuple of values on the right side.
    
    # The values on the right will be automatically assigned to the variables on the left according to their position in the tuple.

# Ex : 1.0

import string


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

x = (1,2,"a",8,{ "key1" : 2, "key2" : 3 },9) # dictionarie in tuple.
a, b, c, d, e, f = x
print("a==>",a,"b==>",b,"c==>",c,"d==>",d,"e==>",e,"f==>",f) 
    # o/p: a==> 1 b==> 2 c==> a d==> 8 e==> {'key1': 2, 'key2': 3} f==> 9

#-----------------------------------------------------------------------------------------------------#

#-------------------------#
# Unpacking List(ordered-mutable) :
#-------------------------#

# Ex : 1

a, b, c, d = [1, '2', {1,2}, 2.3] # list
print(a,b,c,d) # o/p: 1 2 {1, 2} 2.3
print(type(b)) # o/p: <class 'str'>

# Ex : 2

a,b,c,d = [ "5", 10 + 12j, 8.9, ("A", 10 + 12j) ] 
print(a, type(a))   # o/p: 5 <class 'str'>
print(b, type(b))   # o/p: (10+12j) <class 'complex'>
print(c, type(c))   # o/p: 8.9 <class 'float'>
print(d, type(d))   # o/p: ('A', (10+12j)) <class 'tuple'>

#-----------------------------------------------------------------------------------------------------#

#----------------------------------------#
# Unpacking dictionarie(ordered-mutable) :
#----------------------------------------#

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
    } # if duplicate keys exists in dictionarie only last key is considered all the keys before last one will be ignored.
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

#---------------------------------#
# Unpacking Set(Unordered-mutable):
#---------------------------------#

    # in case of unordered iterables like a set(duplicate elements ignored), 
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

# Ex : 1.7
z = set([frozenset([1,2]), frozenset([3,4])])
print(z)    # o/p : {frozenset({3, 4}), frozenset({1, 2})}
x , y = set([frozenset([1,2]), frozenset([3,4])])
print(x)    # o/p : frozenset({3, 4})
print(y)    # o/p : frozenset({1, 2})
q, w = x
print(q,w)  # o/p : 3 4
e, r = y    
print(e,r)  # o/p : 1 2
        
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

        # unpacking operators are operators that unpack the values from 
        # iterable(lists->mutable,dict->mutable,set->mutable,tuples->immutable and strings->immutable) objects in Python.

#----------------------------------------#        
# Unpacking Operator * (asterisk / star) #
#----------------------------------------#

        # The single asterisk operator * can be used on any iterable(lists,tuples,set and strings) object that Python provides.

#---------------------------------#
# * on String : (Ordered,immutable)
#---------------------------------#

x = "mayur"
print(len(x)) # 5
# print(len(*x)) # TypeError: len() takes exactly one argument (5 given)
print(*x) # m a y u r
print([*x]) # ['m', 'a', 'y', 'u', 'r'] 
print({*x}) # {'r', 'a', 'u', 'm', 'y'}
# print((*x)) # SyntaxError: cannot use starred expression here


#-----------------------------#
# * on List : (Ordered,Mutable)
#-----------------------------#

# Ex : 1.0

my_list = [1, 2, 3]
print(my_list) # o/p : [1, 2, 3]

        # Note how the list is printed, along with the corresponding brackets and commas.
        
        # Now, try to prepend the unpacking operator * to the name of your list:

my_list = [1, 2, 3]
print(*my_list) # o/p: 1 2 3

        # Instead of a list, print() function has taken three separate arguments as the input.
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

# Ex : 3

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list) # o/p :[1, 2, 3, 4, 5, 6]

#------------------------------#
# * on Tuple:(Ordered,immutable)
#------------------------------#

# Ex : 1
tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(*tuple) # o/p : apple banana cherry apple cherry
    # a, b, c, d, e = *tuple # SyntaxError: can't use starred expression here

# Ex : 2

tuple = ("apple",70+55j,True, [29,10.74,"piya",10+20j,0+20j], (4.7,2), {"name" : "mayur", "score" : 100, "complex" : 10+88j, True : True==1}, {"mayur",29,30+40j})
print(*tuple)
string, complex, boolean, list, tuple2, dict, set = tuple
    # o/p : apple (70+55j) True [29, 10.74, 'piya', (10+20j), 20j] (4.7, 2) {'name': 'mayur', 'score': 100, 'complex': (10+88j), True: True} {'mayur', 29, (30+40j)}


#-----------------------------------------------------#
# * on Dictionaries:(Ordered(from version 3.7),Mutable)
#-----------------------------------------------------#

        # unpacking dictionarie with * , only keys will be unpacked.

# Ex : 1

a = {
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }       # if duplicate keys exists in dictionarie only last key is considered all the keys before last one will be ignored.
print(*a)   # unpacking dictionarie with * , only keys will be unpacked.
    # o/p: mayur priyanka

# Ex : 2

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

# Ex : 3

a1 = {1 : "a", 2 : "b"}
a2 = {3 : "c", 4 : "d"}
a3 = {5 : "e", 6 : "f"}

d1 = {*a1,*a2,*a3}
print(d1) # o/p :{1, 2, 3, 4, 5, 6}

#--------------------------#
# * on Set:(Ordered,Mutable)
#--------------------------#

# Ex : 1
set = {'a', 'e', 'i', 'o', 'u'}
print(*set) # o/p : i o e u a

# Ex : 2
set = {100,500,'s',50}
print(*set) # o/p : s 50 100 500

# Ex : 3
set = {100,170,180,160,100}
print(*set) # o/p : 160 100 170 180

# Ex : 4
fset = set([frozenset([1,2]), frozenset([3,4])])
print(*fset) # o/p : frozenset({3, 4}) frozenset({1, 2})
a,b = [*fset]
print(*a) # o/p : 3 4
print(*b) # o/p : 1 2

# Ex : 5
fset = set(frozenset(["mayur",4,10+20j]))
print(*fset) # o/p : 4 mayur (10+20j)
a,b = [*fset]
print(type(a),type(b)) # o/p : <class 'int'> <class 'str'> <class 'complex'>
print(a,b) # o/p : 4 mayur (10+20j)


#-----------------#
# * on generators :
#-----------------#

# Ex : 1

gen = (2 ** x for x in range(3))
print(*gen)  # o/p : 1 2 4
print(type(gen)) # o/p: <class 'generator'>
a, b, c = gen # ValueError: not enough values to unpack (expected 3, got 0)
print(a,b,c) # Not executed
print(type(a),type(b),type(c)) # Not executed
    # o/p : 
        # 1 2 4
        # <class 'generator'>
        # ValueError: not enough values to unpack (expected 3, got 0)
        
# Ex : 2
gen = (2 ** x for x in range(3))
print(type(gen)) # o/p: <class 'generator'>
a, b, c = gen # Unpacking generators
print(a,b,c) # o/p: 1 2 4
print(type(a),type(b),type(c)) # <class 'int'> <class 'int'> <class 'int'>
print(*gen) 

    # o/p : 
        # <class 'generator'>
        # 1 2 4
        # <class 'int'> <class 'int'> <class 'int'>

# Ex : 3
    # generator unpacking inside a list
g1 = (x for x in range(3))
g2 = (x**2 for x in range(2))
print([1, *g1, 2, *g2]) # o/p: [1, 0, 1, 2, 2, 0, 1]

# equal to
g1 = (x for x in range(3))
g2 = (x**2 for x in range(2))
print([1] + list(g1) + [2] + list(g2)) # o/p: [1, 0, 1, 2, 2, 0, 1]

# Ex : 4
    # generator unpacking inside a set

g = (x for x in [5, 5, 6, 6])
print({*g}) # o/p: {5, 6}


# Ex : 5
    # generator unpacking inside a function
print(*(x for x in range(3))) # o/p: 0 1 2

# Ex : 6 (generator Unpacking and Packing to variable)
g = (x for x in range(6))
a, b, *c, d = g # unpacking first second generator values to a, b and last value to d which are mandatory variables
                # Packing remaining generator values to c
print(a, b, d) # o/p: 0 1 5
print(c) # o/p : [2, 3, 4]


#--------------------------------------------------------------------------------------------------------------------------#


#-----------------------------#
# Packing With the * Operator :
#-----------------------------#

        # The * operator is known, in this context, as the tuple (or iterable) unpacking operator.
        # It extends the unpacking functionality to allow us to collect or "pack" multiple values in a single variable.
        

        # Converting variable-length iterable in single variable into a list # tricky concept

# Ex : 1(on String-immutable)

        # When you use the unpacking operator with single variable assignment, 
        # Python requires that your resulting variable is either a list or a tuple.

        # *a = "RealPython"
        # print(a) # SyntaxError: starred assignment target must be in a list or tuple

        # if you want to unpack all items of the variable-length iterable into a single variable, a, 
        # then you need to add the comma (,) without naming a second variable.
        # Python will then unpack all items from right side into the first named variable, which is a list.
        # here we have to use tuple unpacking in combination with the unpacking operator *.

*a, = "RealPython"  # There’s unpacking operator *, followed by a variable, and comma, and an assignment.
print(a)    # o/p : ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

        # The comma after the "a" does the trick.
        # With the trailing comma, you have defined a tuple with only one named variable, "a", which is the list
        # Where is the tuple ????
            # You never get to see the tuple that Python creates in this operation,
            # because you use tuple unpacking in combination with the unpacking operator *.
# Ex : 2(on String-immutable)
        # If you name a second variable on the left-hand side of the assignment, 
        # Python will assign the last character of the string to the second variable, 
        # while "packing" all remaining characters in the list "a"

*a, b = "RealPython"
print(a, type(a))
print(b, type(b))
    # o/p:
        # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o'] <class 'list'>
        # n <class 'str'>

# Ex : 1(on list-->ordered,mutable)

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

# Ex : 2(on list-->ordered,mutable)

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

# Ex : 1(on dictionaries-->ordered,mutable)

*a, = {     # Converting dict of variable-length iterable in single variable a of list type.(only key will be unpacked)
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }
print(a, type(a)) # o/p: ['mayur', 'priyanka'] <class 'list'>

# print(a.items())	# AttributeError: 'list' object has no attribute 'items'
                    # cant use items() function on list (we can only use on dictionaries)

# Ex : 2(on dictionaries-->ordered,mutable)

*a,b = {    # Converting dict type of variable-length iterable in single variable a of list type.
            # Python will assign the last character of the string type to the second variable b and 
            # reamining "packed" into "a" (of list type). 
    'mayur': 200,
    'mayur': 9,
    'mayur': 100,
    'priyanka': 29,
    }
print(a, type(a))   # o/p: ['mayur'] <class 'list'>
print(b, type(b))   # o/p: priyanka <class 'str'>

# print(a.items())	# o/p: AttributeError: 'list' object has no attribute 'items'
                    # cant use items() function on list (we can only use on dictionaries)
# print(b.items())	# AttributeError: 'str' object has no attribute 'items'
                    # cant use items() function on list (we can only use on dictionaries)

# Ex : 3(multiple starred expressions in assignmen)

    # *a,*b = {     # multiple starred expressions in assignment is not allowed
    #     '2': 200,
    #     '2': 9,
    #     2: 100,
    #     1: 29,
    #     } 
    # print(type(a),type(b))
    # print(a,b)
    # o/p: SyntaxError: multiple starred expressions in assignment


# Ex : 1 (on tuple-ordered,immutable)

*a, = (1,2,"a",8,{ "key1" : 2, "key2" : 3 },9) # Converting tuple type variable-length iterable in single variable a of list type.
print(a, type(a)) # o/p: [1, 2, 'a', 8, {'key': 2, 'value': 3}, 9] <class 'list'>

# a.items() # o/p: AttributeError: 'list' object has no attribute 'items'

key1, key2 = a[4]	# Unpack keys
print(key1,key2)    # o/p: key1 key2

value1, value2 = a[4].values() # Unpack values
print(value1,value2) # o/p: 2 3

key1_value1, key2_value2 = a[4].items()	# Unpacking key-value pairs (by default in tuple)
print(key1_value1,key2_value2)  # o/p: ('key1', 2) ('key2', 3)

x, y = key1_value1 # further unpacking tuple data
print(x,y) # o/p: key1 2
w, z = key2_value2 # further unpacking tuple data
print(w,z) # o/p: key2 3


# Ex : 2 (on tuple-ordered,immutable)

*a,b = (1,2,"a",8,9,
        {   
            "key1" : 2, 
            "key2" : 3 
        }
        )   # Converting tuple type of variable-length iterable in single variable "a", of list type.
            # Python will assign the last data from tuple which is of dict type to the second variable b, because b is mandatory

print(a, type(a))   # o/p: [1, 2, 'a', 8, 9] <class 'list'>
print(b, type(b)) 	# o/p: {'key1': 2, 'key2': 3} <class 'dict'>

key1, key2 = b  # Unpack keys
print(key1,key2) # o/p: key1 key2

value1, value2 = b.values() # Unpack values
print(value1,value2) # o/p: 2 3

key1_value1, key2_value2= b.items() # Unpacking key-value pairs
print(key1_value1, key2_value2) # o/p: ('key1', 2) ('key2', 3)

# Ex : 3 (on tuple-->ordered,immutable)

*a,b = (1,2,"a",8,9,
        {   
            "key1" : 2, 
            "key2" : 3 
        }
        )   # Converting tuple type of variable-length iterable in single variable "a", of list type.
            # Python will assign the last data from tuple which is of dict type to the second variable b, because b is mandatory

print(a, type(a))   # o/p: [1, 2, 'a', 8, 9] <class 'list'>
print(b, type(b)) 	# o/p: {'key1': 2, 'key2': 3} <class 'dict'>

key1_value1, key2_value2 = b.items()    # Unpacking key-value pairs in tuple
print(key1_value1, key2_value2) # o/p: ('key1', 2) ('key2', 3)

key1, value1 = key1_value1  # unpacking data, key and value from tuple
key2, value2 = key2_value2  # unpacking data, key and value from tuple
print(key1,key2) # o/p: key1 key2
print(value1,value2) # o/p: 2 3


# Ex : 4 (on tuple-->ordered,immutable)

*a, b, c, d = 1, 2, 3 # Packing no values in a (a defaults to empty []) because b, c, and d are mandatory
print(a, b, c, d) # o/p: [] 1 2 3

# Ex : 1 (on Set-unordered,mutable)
    
    # set,lists and dictionaries are mutable and unhashable, so they can’t be "Set" elements.
    # a, b, *c = {1, "abc", [1,2], 2.3} # TypeError: unhashable type: 'list'
    # a, *b, c = {1, "abc", {"a":1,"b":2}, 2.3} # TypeError: unhashable type: 'dict'
    # a, *b, c = {1,"abc",{1,2},2.3} # TypeError: unhashable type: 'set'
    
a, b, *c = {1, "abc", (1,2), 2.3}   # unpacking Set data # a and b are mandatory referance variables
                                    # i.e at least one data will be unpacked in a and b each from set.
                                    # which one data will go to a and b each ???
                                            # actualy we cant predict because sets are unordered by rules 
print(a, type(a))
print(b, type(b))
print(c, type(c))

    # o/p : (1st run)                               (2nd run)
            # (1, 2) <class 'tuple'>                # 1 <class 'int'>
            # 1 <class 'int'>                       # 2.3 <class 'float'>
            # [2.3, 'abc'] <class 'list'>           # [(1, 2), 'abc'] <class 'list'>
    
    # Note- Sets are unordered so every time you run the program the output will vary 
    
    # Unordered means : element position or order of insertion are "not" recorded as defined by programmer.
    # Oredred means : element position or order of insertion are recorded as defined by programmer. 


# Ex : 2 (on set-mutable)

a, *b, c = {"5",6}  # a and c are mandatory referance variables so b contains empty list.
                    # i.e at least one data will be unpacked in a and c each from set.
                                    # which one data will go to a and b each ???
                                            # actualy we cant predict because sets are unordered by rules
print(a, type(a)) 
print(b, type(b))
print(c, type(c))

    # o/p : 
        # 6 <class 'int'>
        # [] <class 'list'>
        # 5 <class 'str'>

# Ex : 3 (on frozenset-immutable)

    # A frozenset is an "unordered" and "unindexed" collection of unique elements. It is "immutable" and it is "hashable".
    # Frozen set is just an immutable version of a Python set object.
z = set([frozenset([1,2,5,8]), frozenset([3,4,8,8])])
print(z)
x , y = set([frozenset([1,2,5,8]), frozenset([3,4,8,8])])
print(x)
print(y)
*s, = x
print(s)
*m,  = y
print(m)
    # o/p:
        # {frozenset({8, 1, 2, 5}), frozenset({8, 3, 4})}
        # frozenset({8, 1, 2, 5})
        # frozenset({8, 3, 4})
        # [8, 1, 2, 5]
        # [8, 3, 4]


# Ex : 1 (on generator)

*g, = (x for x in range(6))
print(g) # o/p : [0, 1, 2, 3, 4, 5]

# Ex : 1(on callable object)
def test_type(*args):
    print(type(args)) # o/p: <class 'tuple'>
    print(args) # o/p : (1, 2, 4, 'a string')
test_type(1, 2, 4, 'a string')

#-------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------#        
# Unpacking Operator ** (double asterisk / star) #
#------------------------------------------------#
        

        # the ** operator is called the dictionary unpacking operator.
        # the double asterisk operator ** can only be used on "dictionaries".
        # ** unpacking operator unpack key and values also.
        # The use of this operator was extended by PEP 448.
        # Now, we can use it in function calls, in comprehensions and generator expressions, and in displays.
        
        # A basic use-case for the dictionary unpacking operator is to merge multiple dictionaries into one final dictionary with a single expression.

# Ex : 0

# **greetings, = {'hello': 'HELLO', 'bye':'BYE'} # SyntaxError: invalid syntax

# Ex : 1
print({**{'vanilla':3, 'chocolate':2}, 'strawberry':2})
    # o/p: {'vanilla': 3, 'chocolate': 2, 'strawberry': 2}

# Ex : 2
        # numbers = {"one" : 1, "two" : 2, "three" : 3}
        # letters = {"a" : "A", "b" : "B", "c" : "C"}
        # combination = {numbers,letters} # TypeError: unhashable type: 'dict'
        # print(combination)
numbers = {"one" : 1, "two" : 2, "three" : 3}
letters = {"a" : "A", "b" : "B", "c" : "C"}
combination = {**numbers,**letters}
print(combination) # o/p : {'one': 1, 'two': 2, 'three': 3, 'a': 'A', 'b': 'B', 'c': 'C'}

        # If we use the dictionary unpacking operator inside a dictionary display, 
        # then we can unpack dictionaries and combine them to create a final dictionary that includes the key-value pairs of the original dictionaries

# Ex : 3
    # if the dictionaries we're trying to merge have repeated or common keys,
    # then the values of the right-most dictionary will override the values of the left-most dictionary.

letters = {"a" : "A", "b" : "B", "c" : "C"}
vowels = {"a" : "a", "e" : "e", "i" : "i", "o":"o","u":"u"}
combination = {**letters,**vowels}
print(combination) # o/p : {'a': 'a', 'b': 'B', 'c': 'C', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'}

        # Python starts adding the key-value pairs from left to right. If, in the process, Python finds keys that already exit, 
        # then the interpreter updates that keys with the new value.

# Ex : 4
    # ** in function call.
def add(one,two,three):
    print(one+two+three)

numbers = {"one" : 1, "two" : 2, "three" : 3}

add(**numbers) 
# o/p: 6

# Ex : 5(packing with **)

def test_kwargs(**packing_with_doublestar):
    print(type(packing_with_doublestar)) # o/p: <class 'dict'>
    print(packing_with_doublestar) # o/p : {'random': 12, 'parameters': 21}

test_kwargs(random=12, parameters=21)

#----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------#        
# Using Packing and Unpacking in Practice #
#-----------------------------------------#
    
    #--------------------#
    # Parallel assignment:
    #--------------------#
        # Parallel assignment allows you to assign the values in an iterable to a tuple (or list) of variables in a single 
        # and elegant statement.


employee = ["Mayur", "29", "Data Scientist"]
name = employee[0]
age = employee[1]
job = employee[2]
print(name,age,job) # o/p: Mayur 29 Data Scientist

    # Using unpacking in Python, we can solve the problem of the previous example with a single, straightforward, and elegant statement. 

name, age , job = ["Mayur", "29", "Data Scientist"]
print(name, age , job) # o/p: Mayur 29 Data Scientist



    #----------------------------------#
    # Swapping Values Between Variables:
    #----------------------------------#
        
        # Another elegant application of unpacking in Python is swapping values between variables without 
        # using a temporary or auxiliary variable. 


a = 100
b = 200
print("a:",a, "b:",b) # o/p : a: 100 b: 200
temp = a
a = b
b = temp
print("a:",a, "b:",b) # o/p : a: 200 b: 100

        # This procedure takes three steps and a new temporary variable. 
        # If we use unpacking in Python, then we can achieve the same result in a single and concise step

a = 100
b = 200
print("a:",a, "b:",b) # o/p : a: 100 b: 200
b,a = a,b 
print("a:",a, "b:",b) # o/p : a: 200 b: 100


    #----------------------------------#
    # Collecting Multiple Values With *:
    #----------------------------------#

        # When we're working with some algorithms, 
        # there may be situations in which we need to split the values of an iterable or a sequence in chunks of values for further processing. 
        # The following example shows how to uses a list and slicing operations to do so

seq = [1, 2, 3, 4]
first, body, last = seq[0], seq[1:3], seq[-1]

print(first, body, last) # o/p: 1 [2, 3] 4

        # Even though this code works as we expect, 
        # dealing with indices and slices can be a little bit annoying, difficult to read, and confusing for beginners.
        # It has also the drawback of making the code rigid and difficult to maintain.
        
        # In this situation, the iterable unpacking operator, *, 
        # and its ability to pack several values in a single variable can be a great tool.

seq = [1, 2, 3, 4]
first, *body, last = seq

print(first, body, last) # o/p: 1 [2, 3] 4
        
        # This makes our code more readable, maintainable, and flexible.
        # You may be thinking, why more flexible?
        # Well, suppose that seq changes its length in the road and you still need to collect the middle elements in body.
        # In this case, since we're using unpacking in Python, no changes are needed for our code to work. 
        # Check out this example:
        
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, *body, last = seq

print(first, body, last) # o/p: 1 [2, 3, 4, 5, 6, 7, 8, 9] 10

        # If we were using sequence slicing instead of iterable unpacking in Python, 
        # then we would need to update our indices and slices to correctly catch the new values.



    #---------------------------------#
    # Dropping Unneeded Values With * :
    #---------------------------------#


        # Another common use-case of the * operator is to use it with a dummy variable name to drop some useless or unneeded values. 
        # Check out the following example:
        
a, b, *_ = 1, 2, 0, 0, 0, 0
print(a)
print(b)
print(_)

    # o/p :
        # 1
        # 2
        # [0, 0, 0, 0]
        
        # For a more insightful example of this use-case, 
        # suppose we're developing a script that needs to determine the Python version we're using. 
        # To do this, we can use the sys.version_info attribute.
        
        # This attribute returns a tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial.
        # But we just need major, minor, and micro for our script to work, so we can drop the rest.

import sys
print(sys.version_info)
major, minor, micro, *_ = sys.version_info
print(major, minor, micro)

    # o/p : 
        # sys.version_info(major=3, minor=10, micro=7, releaselevel='final', serial=0)
        # 3 10 7
        
        
        # The rest of the information is stored in the dummy variable _
        # This can make clear to newcomer developers that 
        # we don't want to (or need to) use the information stored in _ cause this character has no apparent meaning.

    #------------------------------#
    # Returning Tuples in Functions:
    #------------------------------#
    
    
