# read the entire file 
with open("testfile.txt", "r") as f:
    content = f.read()
    print(content)

# read line by line of text from the file
with open("testfile.txt", "r") as f:
    for line in f:
        print(line.strip())
    
