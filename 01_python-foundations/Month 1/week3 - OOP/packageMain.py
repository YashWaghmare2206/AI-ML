
                                # # Examples
# from Packagess.basic import add
#
# print(add(1,2,3,4))

# A package is essentially a directory (folder) that contains multiple module files and a special file named __init__.py.

                        ## 2. Package Structure

# GameProject/
# │
# ├── main.py              <-- Your entry point
# └── GameEngine/          <-- THE PACKAGE
#      ├── __init__.py
#      ├── physics.py       <-- Module 1
#      ├── graphics.py      <-- Module 2
#      └── sounds.py        <-- Module 3


                        ## Import ways for Packages

## Here i can only put dots(.) in the from part not in import part

# 1. Deep import ->      from GameEngine.physics import Gravity
# 2. Module Import  ->   import GameEngine.physics
# 3. The "Alias"  ->     import GameEngine.physics as phys


                            ## Sub packages possible

# AI_Library/
# └── data_processing/     <-- Sub-package
#     ├── __init__.py
#     └── cleaner.py

# 2. What if the 1st folder doesn't have __init__.py?
# In modern Python (version 3.3+), there is a concept called Namespace Packages.
# If Folder1 does not have an __init__.py, but Folder2 does, Python can still find it.
# However, it treats Folder1 as just a "Namespace" (a container) rather than a full Python package.

# Same name py files can exist in different folder in an package no clash

