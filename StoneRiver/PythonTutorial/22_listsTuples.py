
print("\n22: Lists vs Tuples and List Manipulation")
print("=========================================\n")

print("Tuples are immutable - ie, they cannot be changed once defined.")
print("\ttake up less space; quick to iterate thru;")
print("\tusually defined by parens or separated by commas")
print("Lists are mutable - ie, they CAN be changed.")
print("\tusually defined by square brackets")
print("\tcan combines lists, append to them, modify, remove")

## ####################################
## START - define functions
## ####################################

def separator():
    print("\n## ##################################################\n")

def exTuple():
    return 15,19

## ####################################
## END - define functions
## ####################################

## *********************************** 
## START - main program 
## *********************************** 

separator()

print("def exTuple():\n\treturn 15,19\n\na,b=exTuple()\nprint(a,b)",)
a,b = exTuple()
print(a,b)

print("\nx = [1,2,3,4,5,9,8,7,6]\nprint(x)\nprint(x[3])")
x = [1,2,3,4,5,9,8,7,6]
print(x)
print(x[3])

print("\nx.append(12)\nprint(x)")
x.append(12)
print(x)

print("\nx.insert(3,13) - at 4th element(0-based), insert a 13\nprint(x)")
x.insert(3,13)
print(x)

print("\nx.remove(8) - remove the value 8 - only the 1st one\nprint(x)")
x.remove(8)
print(x)

print(x)
print("\nx.index(1) - find where in the list a val exists\nprint(x.index(1))\nprint(x.index(666))")
print("\tcrashes when val is NOT in list - needed TRY-EXCEPT block")
try:
    print(x.index(1))
    print(x.index(666))
except Exception as e:
    print(str(e))

print(x)
print("\nprint(x.count(3))\nprint(x.count(666)) - find how many vals are in a list")
print(x.count(3))
print(x.count(666))

print('\n')
print(x)
print("sort(x)\nprint(x)) - sort a list")
x.sort()
print(x)

print("\nWorks with strings too\ny = ['Spot', 'Cam', 'Jan', 'Dave','Zack']\nprint(y)\ny.sort()\nprint(y)")
y = ['Spot', 'Cam', 'Jan', 'Dave', 'Zack']
print(y)
y.sort()
print(y)

print("\nReverse the order\ny.reverse()\nprint(y)")
y.reverse()
print(y)

print("\n...end of run...")
