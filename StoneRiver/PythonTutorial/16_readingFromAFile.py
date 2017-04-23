

print("\n16: Reading From A File")
print("=========================\n")

## define functions
## ####################################
def separator():
    print("\n\n## ##################################################")

## ####################################

separator()

print("\nopen() is a built-in function\n\tuse 'r.read()' to read from existing file")
print("\treadMe = open('exampleWrite.txt', 'r').read()\n\tprint(readMe)\n\n")

readMe = open('exampleWrite.txt', 'r').read()
print(readMe)

print("\nto get the contents from a file into a list separated by newlines, use split() as follows:")
print("\tsplitMe = readMe.split('\\n')\n\tprint(splitMe)\n")

splitMe = readMe.split('\n')
print(splitMe)

print("\nsplit moves everything into a list, to access a single line, index the list array\n\tprint(splitMe[2])")
print(splitMe[2])

print("\ncan accomplish the same thing at read time by using readlines - but this keeps the newline character")
print("\treadMe2 = open('exampleWrite.txt', 'r').readlines()\nprint(readMe2)")
readMe2 = open('exampleWrite.txt', 'r').readlines()
print(readMe2)

separator()
