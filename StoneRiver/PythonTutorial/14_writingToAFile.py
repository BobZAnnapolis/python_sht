

print("\n14: Writing To A File")
print("=====================\n")

## define functions
## ####################################
def separator():
    print("\n\n## ##################################################")

## ####################################

separator()

print("'\nopen() is a built-in function'\n\nwriteMe = 'Example text'\nsaveFile = open('exampleWrite.txt', 'w')\nsaveFile.write(writeMe)\nsaveFile.close()")

writeMe = "Example text\n"
saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close()

separator()
