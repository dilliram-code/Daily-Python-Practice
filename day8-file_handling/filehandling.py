# read the entire file 
with open("day7-file_handling/testfile.txt", "r") as f:
    content = f.read()
    print(content)


# read line by line of text from the file
with open("day7-file_handling/testfile.txt", "r") as f:
    for line in f:
        print(line.strip())
    

# create the file, if already exits then it overwrites on that file.
with open("day7-file_handling/file2.txt", "w") as f:
    f.write("This text is written in the file as a sample text.")

# read in binary mode
with open("day7-file_handling/file2.txt", "rb") as f:
    binary = f.read()
    print(binary)

# append the text in the existing file to the end 
with open("day7-file_handling/file2.txt", "a") as f:
    f.write("\nThis text has be appened.")


# Working with binary files
# copy the image in pexels-1.jpg to recent.jpg
with open("day7-file_handling/recent.jpg", "wb") as f:
    with open("day7-file_handling/pexels-1.jpg", "rb") as original:
        f.write(original.read())
        
        
# Note: The with statement automatically closes files after use — avoids memory leaks.

# File existence check
import os
if os.path.exists("file3.txt"):
    print("file exists!")
else: 
    print("file doesn't exist!")