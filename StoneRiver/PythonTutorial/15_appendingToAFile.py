

print("\n15: Appending To A File")
print("=======================\n")

## define functions
## ####################################
def separator():
    print("\n\n## ##################################################")

## ####################################

separator()

print("\nopen() is a built-in function\n\tuse 'a' to add to existing text, will create file if it has to")
print("appendMe = 'Appended text added to an existing file'\nsaveFile = open('exampleWrite.txt', 'a')\nsaveFile.write(writeMe)\nsaveFile.close()")

appendMe = "Appended text added to an existing file\n"
saveFile = open('exampleWrite.txt', 'a')
saveFile.write(appendMe)
saveFile.close()

separator()
