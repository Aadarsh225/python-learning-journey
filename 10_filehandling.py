# with open ("example.txt","r") as file:
#      content = file.read()
#      print(content)
# with open ("example.txt","a") as file:  ## "a" for append
#     file.write("\nThis is an additional line.")

# with open ("example.txt","r") as file:    
#       content = file.read()
#       print(len(content))
#       file.close()

# with open ("practice.txt","w") as file:  ## "w" for write (overwrites the file)
#     file.write("This is a new file created for practice.")

# with open ("example.txt","r") as file:
#     for line in file:
#         print(line.strip())  ## strip() removes the newline character

# with open ("example.txt","r") as file:
#     lines = file.readlines()
#     print(lines)

import os


with open("example.txt", "w") as file:
    file.writelines(["Line 1\n", "Line 2\n"])

if os.path.exists("example.txt"):
    print("File exists.")