# file = open("testdata.txt", "r") #("filename", "mode")
#         #
#
# file.close()
from os import write

#Automatically close the file after the block ends
# with open("testwrite.txt", 'r') as file:
#     obj = file.read()


# Writing Text to a File

with open("../testwrite.txt", "r+") as file:

    file.write("Appending this lin.\n")
    file.write("Writing to a file in Python.\n")
    file.write("HELLO THIS IS ME wirthing the  in Python.\n")
# with open("testwrite.txt", "r") as readdd:
    obj = file
    print(obj)



