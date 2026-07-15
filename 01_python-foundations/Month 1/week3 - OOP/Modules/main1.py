
# A module is simply a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.

## Folder Placement

# 1. Scenario A: Same Folder (The Simple Way)
# If main.py and converter.py are in the same folder, life is easy. Python sees them as "neighbors."
# Project/
# ├── main.py
# └── converter.py


# 2. Scenario B: Sub-Folder (The Organized Way)
# This is what you are doing now. main.py is the "Boss" in the main folder,
# and Modules is a "Drawer" (sub-folder) full of tools.
# Project/
# ├── main.py
# └── Modules/            <-- Sub-folder (One level LOWER)
#     └── converter.py


                            ## Importing Techniques

# 1. Standard Import ->   import math  (But if contains class we have to write " math.classname ")
# 2. Alias Import ->      import pandas as pd
# 3. Specific ->          import from math import pi
# 4. Wildcard import ->   from math import.*

                            ## How python look for files

# 1. The Directory of the script you are currently running.
# 2 .PYTHONPATH (an environment variable).
# 3. Standard Library directories.
# 4. Site-packages (where pip installs things).

                    ## To see were python is looking for
# import sys
# print(sys.path)

                ## TO CHECK WHICH CLASSE FUNCTION VARIABLES IT CONTAINS

# import math
# print(dir(math))
# # Output: ['__doc__', 'acos', 'asin', 'atan', 'ceil', 'cos', 'pi', ...]

                                    ## Module Reloading

# If you change the code in a module while a program is running (like in a Jupyter notebook),
# Python will not automatically see the changes if you just type import again.
# You must use the importlib library:

# import importlib
# import converter
# importlib.reload(converter)


# # 1st Way to import module
# import converter
# c = converter.Converter()
#
# print(c.to_celsius(100))


# 2nd Way to import Module if the main file out