import shutil

# copy: copy the content of source file to destination file
shutil.copy("shutil1.txt", "shutil2.txt")
print("file copied")


# copy2: Same as copy but preserves metadata (timestamps, permissions).
shutil.copy2("source.txt", "destination.txt")
print("source file copied to its destination")


# copyfile: Copies file contents only (no permissions, no metadata).
shutil.copyfile("source.txt", "destination.txt")

