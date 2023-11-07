import random

random_number = random.randint(0,55)
# print(random_number)
rand = random.random() *1000000000
# print(rand)

list = ["star plus","DD1","Aaj Tak","CodeWithHarry"]
shuffle = random.choice(list)
print(shuffle)

# Using Python External and built in modules:
"""
     In Python, a module can be defined sd file containing a runnable python code.
    The extension used by modules in python is .py. Hence any simple file containing Python Code can be cnsidered as module if its extension is .py.
   The file and module names are the same; hence we can call a module only by name without using extension.
  Along with this a module can define functions, classes and variables.

"""

# NOTE:- There are two types of modules.
"""
(1) Built-in
(2) External
"""

# Built-in Modules:-
""" 
 Built-in modules are already installed in Pyhon by default. We can import a module in Python by using import statement along with specific module name.
We can also access built-in module files and read the Python code present in them. Newly integreated modeules are added in Python with each update.

Some modules names are as follows
(1) calendar :  Used in case we are working with calendar
(2) random   :  Used for generating random numbers within certain defined limits.
(3) enum     :  used while working with enumeration class.
(4) html     :  for handling and manipulating code in HTML
(5) math     :  for working with math functions such as sin, cos, etc
(6) runpy    :  runpy is an important module as it locates and runs Python modules without importing them first.
"""

# External Modules:-
"""
        External modules have to be downloaded externally; they do not already present like built-in ones.
       Installing them is easy and can be done by using the command "pip install module_name" in compiler terminal
      We cannot remember all modules cause there are to many modules it is hard even for best piro programmer.
     Hence we should search module and learn how to use it as process is same for all.
    Module make life easier for programmer, apart from other programming languages Python provides us lot of modules that make our coding much easier
   because we do not have to write all code for themselves. We can directly access a module for specific task.
  we should not concern ourselves with code written inside the modules; instead, we can search the internet for function and properties.
 If we are not satsfied with available module work or could not find module that could help us in required manner, we can create our own module by making .py extension.
The module file will be like any other file you see in Python, the difference will just arise in extension.
"""

