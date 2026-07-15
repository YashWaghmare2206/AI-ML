
# The main file is outside the Practice folder



"""
TOPIC 5: MODULES AND PACKAGES
-----------------------------
Instructions: Create the following structure in your project.
"""

# 1. MEDIUM QUESTION: The "MathTool" Module
# - Create a file named 'math_tool.py'.
# - Inside it, define a function 'cube(n)' and a class 'Calculator' with a 'multiply(a, b)' method.
# - In your 'main.py', import only the 'cube' function and the 'Calculator' class.
# - Test: Print the cube of 3 and the result of 5 * 4 using the imported class.


# 2. MEDIUM QUESTION: The "__name__" Protection
# - In your 'math_tool.py' file, add a print statement: "MathTool Loaded!"
# - Wrap that print statement inside an 'if __name__ == "__main__":' block.
# - Test: Run 'math_tool.py' directly (you should see the print).
# - Test: Run 'main.py' (you should NOT see the print).


# 3. HARD QUESTION: The "SuperPackage" Construction
# - Create a folder named 'AppPackage'.
# - Inside 'AppPackage', create an empty '__init__.py'.
# - Inside 'AppPackage', create a file 'string_logic.py' with a function 'reverse_str(s)'.
# - CHALLENGE: In 'AppPackage/__init__.py', write code to import 'reverse_str' from '.string_logic'.
# - Test: In your 'main.py' (OUTSIDE the folder), use this specific import:
#   'from AppPackage import reverse_str'
#   (Notice how we skip the filename '.string_logic' because of the __init__ shortcut!)


# 1.

def cal_cube(n):
    return n * n *n

class Calculator:

    def multiply(self , a,b):
        return a * b

if __name__ == "__main__":
    print("MathTool Loaded")




