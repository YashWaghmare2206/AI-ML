from multiprocessing.pool import ApplyResult

from ModulesAndPackages import Calculator,cal_cube

n = cal_cube(5)
print(n)

c = Calculator()
print(c.multiply(45 , 5))

# 2.
from AppPackage.string_logic import reverse_str

# To avoid so big import above(2.) you can also add "from AppPackage import string_logic"
# then we have to just write " from .string_logic import reverse_str"

# If __init__.py is...	You must import like this:

# Empty ->	             from AppPackage.string_logic import reverse_str
# Has shortcut code ->    from AppPackage import reverse_str
# Any Case  ->           import AppPackage.string_logic (Then call as AppPackage.string_logic.reverse_str())







