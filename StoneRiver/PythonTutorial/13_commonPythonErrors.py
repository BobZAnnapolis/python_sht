

print("\n13: Common Python Errors & Debugging")
print("====================================\n")

print("Check indenting, typos in variables and function names")
print("When coding, if you get an automatic indent, RED FLAG something is wrong")


def separator():
    print("\n\n====================================")


separator()
print("## Name Error:\nvaraible = 6\nprint(variable)")


separator()
print("## Expected an indent\ndef fcn_1():\n\ndef fcn_2():\n    print(2)")


separator()
print("## Unexpected indext\ndef task():\n    print('1')\nprint('2')\n    print('3'))\n    ^\nIndentationError: unexpected indent")


separator()
print("## EOL While Scanning String\n    print('Hey there how are you?\n                                ^\nSyntaxError: EOL while scanning string literal")


separator()
print("## EOF While Parsing\n    print('Hey there how are you?'\n                                 ^\nSyntaxError: unexpected EOF while parsing")
print("\nAlso occurs when a closing bracket, paren hasn't been supplied")


separator()

