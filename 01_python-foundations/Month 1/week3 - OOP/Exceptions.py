# Below is a **clean, exam-ready list** of **definitions + examples** for **each error type** you asked for.
# You can **memorize or revise directly from this**.
#
# ---
#
# ## 1️⃣ **Syntax Error**
#
# ### **Definition**
#
# Occurs when Python **cannot understand the code structure** due to incorrect syntax.
#
# ### **Example**
#
# ```python
# if x > 5
#     print(x)
# ```
#
# ### **Error**
#
# ```
# SyntaxError: invalid syntax
# ```
#
# ---
#
# ## 2️⃣ **Runtime Error**
#
# ### **Definition**
#
# Occurs **while the program is running**, after successful syntax checking.
#
# ### **Example**
#
# ```python
# x = 10 / 0
# ```
#
# ### **Error**
#
# ```
# ZeroDivisionError
# ```
#
# ---
#
# ## 3️⃣ **Logical Error**
#
# ### **Definition**
#
# Program runs without error but **produces incorrect output** due to wrong logic.
#
# ### **Example**
#
# ```python
# x = 5
# y = 10
# print(x + y * 2)
# ```
#
# ### **Output**
#
# ```
# 25
# ```
#
# (Expected `30`)
#
# ---
#
# ## 4️⃣ **Indentation Error**
#
# ### **Definition**
#
# Occurs when code blocks are **not properly indented**, which Python requires.
#
# ### **Example**
#
# ```python
# if x > 5:
#     print(x)
# ```
#
# ### **Error**
#
# ```
# IndentationError: expected an indented block
# ```
#
# ---
#
# ## 5️⃣ **Type Error**
#
# ### **Definition**
#
# Occurs when an operation is performed on **incompatible data types**.
#
# ### **Example**
#
# ```python
# x = 5 + "10"
# ```
#
# ### **Error**
#
# ```
# TypeError: unsupported operand type(s)
# ```
#
# ---
#
# ## 6️⃣ **Name Error**
#
# ### **Definition**
#
# Occurs when a variable or function name is **not defined**.
#
# ### **Example**
#
# ```python
# print(a)
# ```
#
# ### **Error**
#
# ```
# NameError: name 'a' is not defined
# ```
#
# ---
#
# ## 7️⃣ **Key Error**
#
# ### **Definition**
#
# Occurs when trying to access a **non-existing key in a dictionary**.
#
# ### **Example**
#
# ```python
# d = {"a": 1}
# print(d["b"])
# ```
#
# ### **Error**
#
# ```
# KeyError: 'b'
# ```
#
# ---
#
# ## 8️⃣ **Attribute Error**
#
# ### **Definition**
#
# Occurs when an object **does not have the specified attribute or method**.
#
# ### **Example**
#
# ```python
# x = 10
# x.append(5)
# ```
#
# ### **Error**
#
# ```
# AttributeError: 'int' object has no attribute 'append'
# ```
#
# ---
#
# ## 9️⃣ **Index Error**
#
# ### **Definition**
#
# Occurs when trying to access an **index that is out of range**.
#
# ### **Example**
#
# ```python
# lst = [1, 2, 3]
# print(lst[5])
# ```
#
# ### **Error**
#
# ```
# IndexError: list index out of range
# ```
#
# ---
#
# ## 🔟 **Import Error**
#
# ### **Definition**
#
# Occurs when Python **cannot find or import a module**.
#
# ### **Example**
#
# ```python
# import xyz
# ```
#
# ### **Error**
#
# ```
# ModuleNotFoundError: No module named 'xyz'
# ```
#
# ---
#
# ## 1️⃣1️⃣ **Value Error**
#
# ### **Definition**
#
# Occurs when a function receives the **correct data type but an invalid value**.
#
# ### **Example**
#
# ```python
# int("abc")
# ```
#
# ### **Error**
#
# ```
# ValueError: invalid literal for int()
#     ```
#
# ---
#
# ## 📌 Summary Table (Quick Revision)
#
# | Error Type  | Cause                    |
# | ----------- | ------------------------ |
# | Syntax      | Invalid code structure   |
# | Runtime     | Error during execution   |
# | Logical     | Wrong logic              |
# | Indentation | Incorrect spacing        |
# | Type        | Incompatible data types  |
# | Name        | Variable not defined     |
# | Key         | Dictionary key missing   |
# | Attribute   | Invalid object attribute |
# | Index       | Index out of range       |
# | Import      | Module not found         |
# | Value       | Invalid value            |
#
# ---
from pkg_resources import find_nothing

# Example

n = 10
x = 0
#
# try:
#     print(1)
#     print(2)
#     print(10//x)
# except:
#     print("Bhai answer infinity ♾️♾️ Jayel")
# finally:
#     print("Bhai execute zhala")



a = 14
b = 0
c = 2

try:
    print(1)
    print(2)
    print(a//0)
except ZeroDivisionError as zde:      ## Only executes id deno is zero
    print("zde")
except:
    print("Other Error") # Occurs if error is not Zero in denominator

else:
    print("Executes when code is working perfectly")
finally:
    print("Executes no matter what happens")







