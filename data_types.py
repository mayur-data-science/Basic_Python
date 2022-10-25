#------------#
# Data Types #
#------------#
        # Data Type represents the type of data present inside a variable.
        # In Python we are not required to specify the type explicitly. 
        # Based on value provided,the type will be assigned automatically.
        # Hence Python is dynamically Typed Language.

    # Python contains the following inbuilt data types:
        # 1) Int
        # 2) Float
        # 3) Complex
        # 4) Bool
        # 5) Str
        # 6) Bytes
        # 7) Bytearray
        # 8) Range
        # 9) List
        # 10) Tuple
        # 11) Set
        # 12) Frozenset
        # 13) Dict
        # 14) None

    # Note : Python contains several inbuilt functions

        # 1) type()  ---> to check the type of variable. 
        # 2) id()    ---> to get address(memory location) of object in decimal form.
        # 3) print() ---> to print the value.

    # In Python everything is an Object.

# 1) int Data Type:

    # We can use int data type to represent whole numbers (integral values) 

    # Ex : 1                              | # Ex : 2                              | # Ex : 3
    # a = 10                              | # b = -10                             | # c = 0
    # print(type(a)) # o/p: <class 'int'> | # print(type(a)) # o/p: <class 'int'> | # print(type(c)) # o/p: <class 'int'>

    # Note: In Python 2 we have long data type to represent very large integral values.
    #       But in Python3 there is no long type explicitly and we can represent long values also by using int type only.

    # We can represent int values in the following ways :
        # 1) Decimal form
        # 2) Binary form
        # 3) Octal form
        # 4) Hexa decimal form

    # 1) Decimal Form ( Base - 10 ) :
            # It is the default number system in Python
            # The allowed digits are: 0 to 9
            # Ex : a = 50

    # 2) Binary Form ( Base - 2 ) :
            # The allowed digits are : 0 & 1
            # Literal value should be prefixed with 0b or 0B
        
        # Ex :                                 | # Ex :                            | # Ex :
        # a = 0B1111                           | # b = 0b111                       | # c = 0b123 # SyntaxError: invalid digit '2' in binary literal
        # print(type(a)) # o/p: <class 'int'>  | # print(type(b)) # <class 'int'>  | # print(c)
        # print(a) # o/p: 15                   | # print(b) # o/p: 7               |

    # 3) Octal Form ( Base - 8 ) :
            # The allowed digits are : 0 to 7 
            # Literal value should be prefixed with 0o or 0O.
        
        # Ex :                                  | # Ex : 
        # a = 0o123                             | # b = 0o786 # SyntaxError: invalid digit '8' in octal literal
        # print(type(a)) # o/p : <class 'int'>  | # print(b)
        # print(a) # 83                         |

    # 4) Hexa Decimal Form (Base - 16) :
            # The allowed digits are: 0 to 9, a-f (both lower and upper cases are allowed) 
            # Literal value should be prefixed with 0x or 0X
        
        # a = 0XFACE                     | # b = 0XBeef                     | # c = 0XBeer # SyntaxError: invalid hexadecimal literal
        # print(type(a)) # <class 'int'> | # print(type(b)) # <class 'int'> | # print(type(c))
        # print(a) # 64206               | # print(b) # 48879               | # print(c)


    # Note: Being a programmer we can specify literal(data) values in decimal, binary, octal and hexa decimal forms.
    # But PVM will always provide values only in decimal form.
    
    # a = 10          | d = 0B10        | b = 0o10       | c = 0X10
    # print(a) # 10   | print(d) # 2    | print(b) # 8   | print(c) # 16