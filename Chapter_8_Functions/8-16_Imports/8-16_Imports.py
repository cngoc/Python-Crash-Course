# Using a program you wrote that has one function in it, store that function
# in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


import imports
imports.display_message()

from imports import display_message
display_message()

from imports import display_message as dm
dm()

import imports as im
im.display_message()

from imports import *
display_message()
