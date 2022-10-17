#----------------#
# RESERVED WORDS :
#----------------#

    # In Python some words are reserved to represent some meaning or functionality.
    # Such types of words are called reserved words.

    # There are 35 reserved words available in Python :

        # True, False, None
        # and, or , not, is 
        # if, elif, else
        # while, for, break, continue, return, in, yield
        # try, except, finally, raise, assert 
        # import, from, as, class, def, pass, global, nonlocal, lambda, del, with
        # async, await

    # Note:

    #     1. All Reserved words in Python contain only alphabet symbols.

    #     2. Except the following 3 reserved words, all contain only lower case alphabet symbols.

    #         True
    #         False
    #         None

    #     Eg: a = true (invalid)
    #         a = True √

import keyword 
print(keyword.kwlist)

# o/p :
    # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
    # 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
    # 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
    # 'return', 'try', 'while', 'with', 'yield']


#-----------------#
# "soft" keywords :
#-----------------#
    # 1) match
    # 2) case
    
        # match and case are better described as "soft" keywords.

        # "soft" keywords means You can keep using “match” or “case” as a variable name in other parts of your program.

        # The match case statement in Python is more powerful and allows for more complicated pattern matching.

match = 10
case = 20

command = 'Hello, World!'
match command:
    case 'Hello, World!':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later')
    case other:
        print('No match found')