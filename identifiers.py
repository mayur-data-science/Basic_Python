#-------------#
# IDENTIFIERS :
#-------------#

        # A Name in Python Program is called Identifier.
        # It can be Class Name OR Function Name OR Module Name OR Variable Name.
        # variable_name = 60
        
#--------------------------------------#
# Rules to define Identifiers in Python:
#--------------------------------------#

    # 1. The only allowed characters in Python are : 
        # alphabet symbols(either lower case or upper case) 
        # digits(0 to 9)
        # underscore symbol(_)

    # By mistake if we are using any other symbol like $ then we will get syntax error.

        # cash = 10 (valid)
        # ca$h =20 (invalid)

    # 2. Identifier should not starts with digit

        # 123total 
        # total123 √

    # 3.Identifiers are case sensitive. Of course Python language is case sensitive language.

total=10
TOTAL=999
print(total) #10
print(TOTAL) #999

#-----------#
# Identifier:
#-----------#

    # 1) Alphabet Symbols (Either Upper case OR Lower case)

    # 2) If Identifier is start with Underscore (_) then it indicates it is private.

    # 3) Identifier should not start with Digits.

    # 4) Identifiers are case sensitive.

    # 5) We cannot use reserved words as identifiers Eg: def = 10

    # 6) There is no length limit for Python identifiers. But not recommended to use toolengthy identifiers.

    # 7) Dollor ($) Symbol is not allowed in Python.


# Q) Which of the following are valid Python identifiers ?

        # 1) 123total (invalid)
        # 2) total123 √
        # 3) python2share √
        # 4) ca$h (invalid)
        # 5) _abc_abc_ √
        # 6) def (invalid)
        # 7) if (invalid)

    # Note: 
        # 1) If identifier starts with _ symbol then it indicates that it is private
        # 2) If identifier starts with __ (Two Under Score Symbols) indicating that strongly private identifier.
        # 3) If the identifier starts and ends with two underscore symbols then the identifier is language defined special name, which is also known as magic methods.
        # 4) Eg: __add__