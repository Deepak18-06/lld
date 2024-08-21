# import sys
# import os
# sys.path.insert(0, os.path.dirname(__file__))
# print(os.path.dirname(__file__))


import sys
import os
current_directory = os.path.dirname(os.path.realpath(__file__))
print(current_directory)
parent_directory = os.path.dirname(os.path.dirname(current_directory))
print(parent_directory)
sys.path.insert(0, parent_directory)

print(parent_directory)
