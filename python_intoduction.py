#---------------------#
# Python Introduction :
#---------------------#

    # Python is a general purpose high level programming language.
        # General Purpose --> Common purpose(That means we can use this programming language anywhere)
        # High level programming language --> we need not to take care low level things( address of varibale ,pointers,Memory utilization , Datatype)
        # such type of programming language are known as programmer friendly programing language.


    # Python was developed by Guido Van Rossam in 1989 while working at National Research Institute at Netherlands.
    # But officially Python was made available to public in 1991. The official Date of Birth for Python is : Feb 20th 1991.
    # Python is recommended as first programming language for beginners.
    # Python is implemented before java.(1996 jdk 1.0).

    # The name Python was selected from the TV Show "The Complete Monty Python's Circus", which was broadcasted in BBC from 1969 to 1974.

    # Guido developed Python language by taking almost all programming features from different languages
            # 1.Functional Programming Features from C 
            # 2.Object Oriented Programming Features from C++
            # 3.Scripting Language Features from Perl and Shell Script 
            # 4. Modular Programming Features from Modula-3

    # Most of syntax in Python Derived from "C" and "ABC" languages.

    # Where we can use Python:
        # 1.Machine learning Algorithms--> scikit learn
        # 2.Web Applications --> Django , Flask , tornado etc
        # 3.Data science and Data Analysis --> Numpy , scipy, Pandas
        # 4.Data visualization --> Matplotlib, Seaborn etc..
        # 5.Iot --> Internet of Things --> AI --> Python
        # 6.Game --> Pygame
        # 7.Desktop Application--> Tkinter, flet
        # 8.For developing database Applications
        # 9.For Network Programming

    # Worst case of using Python:
        # 1.Mobile Application --> Java and Kotlin
        # 2.For implementing compiler --> High level programming and it is slow as compared to java

    # Note:
        # Internally Google and Youtube use Python coding.
        # NASA and Nework Stock Exchange Applications developed by Python.
        # Top Software companies like Google, Microsoft, IBM, Yahoo, dropbox using Python.

    
    # Features of Python:
    
        # 1) Simple and easy to learn:
        #     Python is a simple programming language. When we read Python program,we can feel like reading english statements.
        #     The syntaxes are very simple and only 30+ kerywords are available.
        #     When compared with other languages, we can write programs with very less number of lines. Hence more readability and simplicity. 
        #     We can reduce development and cost of the project.

        # 2) Freeware and Open Source: 
        #     We can use Python software without any licence and it is freeware. 
        #     Its source code is open, so that we can we can customize based on our requirement. 
        #     Eg: Jython is customized version of Python to work with Java Applications.

        # 3) High Level Programming language: 
        #     Python is high level programming language and hence it is programmer friendly language. 
        #     Being a programmer we are not required to concentrate low level activities like memory management and security etc.

        # 4) Platform Independent: 
        #     Once we write a Python program,it can run on any platform without rewriting once again. 
        #     Internally PVM is responsible to convert into machine understandable form.


        # 5) Portability: 
        #     Python programs are portable. 
        #     ie we can migrate from one platform to another platform very easily. 
        #     Python programs will provide same results on any paltform.

        # 6) Dynamically Typed: 
        #       In Python we are not required to declare type for variables. 
        #       Whenever we are assigning the value, based on value, type will be allocated automatically.Hence Python is considered as dynamically typed language. 
        #       But Java, C etc are Statically Typed Languages b'z we have to provide type at the beginning only.
        #       This dynamic typing nature will provide more flexibility to the programmer.

        # 7) Both Procedure Oriented and Object Oriented: 
        #       Python language supports both Procedure oriented (like C, pascal etc) and object oriented (like C++, Java) features. 
        #       Hence we can get benefits of both like security and reusability etc

        # 8) Interpreted Programming langauge : (Line by line execution)
        #       We are not required to compile Python programs explcitly. Internally Python interpreter will take care that compilation. 
        #       If compilation fails interpreter raised syntax errors. 
        #       Once compilation success then PVM (Python Virtual Machine) is responsible to execute code Line by line execution.
        #   @ Compiled Programming language --> Exection will done atonce.(whole file will be executed atonce)
        #   @ interpreted Programming Languages -->Exection will be done line by line

        # 9) Extensible:
        #       We can use other language programs in Python. 
        #       The main advantages of this approach are:
        #       We can use already existing legacy non-Python code 
        #       We can improve performance of the application

        # 10) Embedded: 
        #       We can use Python programs in any other language programs. i.e we can embedd Python programs anywhere.

        # 11) Extensive Library: 
        #       Python has a rich inbuilt library. 
        #       Being a programmer we can use this library directly and we are not responsible to implement the functionality. Etc.


    # Flavors of Python: 
    #     1) CPython: It is the standard flavor of Python. It can be used to work with C lanugage Applications. 
    #     2) Jython OR JPython: It is for Java Applications. It can run on JVM 
    #     3) IronPython: It is for C#.Net platform 
    #     4) PyPy:The main advantage of PyPy is performance will be improved because JIT compiler is available inside PVM.
    #     5) RubyPython: For Ruby Platforms 
    #     6) Anaconda Distribution: It is specially designed for handling large volume of data processing. 
    
    # Python Versions: 
    #         Python 1.0V introduced in Jan 1994
    #         Python 2.0V introduced in October 2000
    #         Python 3.0V introduced in December 2008
    #           Note: Python 3 won't provide backward compatibility to Python2 i.e 
    #                 there is no guarantee that Python2 programs will run in Python3. 
    #         Current versions Python 3.10.7 | Python 2.7.13
    
    # IN C++
    # header file
    # int main()
    # {
    # cout<<"Hello world";
    # }
    
    #In JAVA
    # class test{
    # public static void main("String[] args"){
    # system.out.println("hello world");
    #   }
    # }
    
    #In Python
print("Hello world")

    # Note: if number of lines of code is increased then the chances of getting error(making mistake) is higher