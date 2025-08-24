import os 
import sys

# get the os name
print(os.name)  # 'nt' for windows

# get current working directory
print(os.getcwd())  

# get the platform
print(sys.platform)  # 'win32' for windows

# create directory
os.mkdir("day13-functionsDive")
