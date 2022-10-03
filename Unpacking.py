# Unpacking in Python: 
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
        
        # operation that consists of assigning an iterable of values of right hand side to a left hand side
        # {set} or dict {key:values} of variables in a single assignment statement is not allowed.
        # Ex : 0.0
            # {a,b,c} = 1,2,3 # SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
            # print("a:",a,"b:",b,"c:",c)
        
        # Ex : 0.1
            # {a : 4 , b : 5, c : 6} = 1,2,3 # SyntaxError: cannot assign to dict literal here. Maybe you meant '==' instead of '='?
            # print("a:",a,"b:",b,"c:",c)
        
# iterable unpacking :
        # Any iterable in python, a list(ordered), dict(ordered), tuple(ordered), set(unordered) is said to have a pack of values.(String is also iterable object)
        # We can unpack the values from an iterable into a individual variables.
        
        # As of Python version 3.10.7, dictionaries are "ordered". In Python 3.6 and earlier, dictionaries are unordered.
        # Note: in case of unordered iterables like a set(duplicate elements not considered), the sequence of values unpacked into different variables is not guaranteed.
        # Once a set is created, you cannot change its items, but you can remove items and add new items.

# Unpacking Tuples(ordered) : 
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

