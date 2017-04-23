
print("\n04: Variable Examples\n")
print("=====================\n")

## act as placeholders
## useful for not hard-coding data
## dynamically changes

## define by setting
print( "\nvar print integer\texVar = 100 \nprint(exVar)")
exVar = 100
print( exVar)

print( "\nvar print strings\nexVar = '100' \nprint(exVar)")
exVar = '100'
print( exVar)

print( "\nvar print operation\nexVar = 100 \nprint(exVar)\nopVar=exVar/5.3\nprint(opVar)")
exVar = 100
print( exVar)
print( "\nprint operation\nexVar = 100 \nprint(exVar)\nopVar=exVar/5.3\nprint(opVar)")
opVar=exVar / 5.3
print(opVar)

## limitations, cannot start a var name with a number
print( "\nvar name limitations, cannot start with a number\n100exVar = 100 \nprint(100exVar)")
## uncomment next line to see execution error
## 100exVar = 100

## if u really want to have a # start it, precede with an _
print( "\nvar name can start w/underscore and then have a # in name\n_100exVar = 100 \nprint(_100exVar)")
_100exVar = 100
print( _100exVar)
