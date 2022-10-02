# Iterables: Python has four built-in iterable types: list, dict, tuple, and set
    # In Python, an iterable object (or simply an iterable) is a collection of elements that you can loop (or iterate) through one element at a time.
    
    # An iterable is ordered if you can retrieve its elements in a predictable order
    # An iterable is mutable if you can change which elements it contains
    
# list: 
    # an Ordered, mutable collection of elements
# Ex : 1.0
a, b, c, d = [1, '2', {1,2}, 2.3] # list
print(a,b,c,d) # o/p: 1 2 {1, 2} 2.3


# dict: 
    # an Ordered, mutable collection of key-value pairs
    # As of Python version 3.10.7, dictionaries are "ordered". In Python 3.6 and earlier, dictionaries are unordered.
# tuple: 
    # an Ordered, immutable collection of elements
# set: 
    # an unordered, mutable collection of unique elements
    
    # A characteristic feature of sets is that each element can occur at most once (duplicates are ignored)
    
# Ex : 1.2
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
x = {100,170,180,160,100}
print(x)
a,b,c,d,e = x
print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e) 
# o/p:
    # {160, 100, 170, 180}
    # ValueError: not enough values to unpack (expected 5, got 4)
