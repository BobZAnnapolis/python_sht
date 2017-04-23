
print("\n23: Dictionaries")
print("================\n")

print("Lot like a database")
print("\tKey-value pair\nunordered groups of data")
print("\tall keys have to be unique; mutable-ie, can change")
print("\tdefined using {}")

## ####################################
## START - define functions
## ####################################

def separator():
    print("\n## ##################################################\n")

## ####################################
## END - define functions
## ####################################

## *********************************** 
## START - main program 
## *********************************** 

separator()

gradeDict = { 'Kelly':89,
              'David':65,
              'Jack':95,
              'Samantha':78
            }

print("print(gradeDict)")
print(gradeDict)

print("\nprint(gradeDict['David'])")
print(gradeDict['David'])

print("\nModify an entry\ngradeDict['David'] = 56\nprint(gradeDict)")
gradeDict['David'] = 56
print(gradeDict)

print("\nAdd a new entry\ngradeDict['Jesse'] = 92\nprint(gradeDict)")
gradeDict['Jesse'] = 92
print(gradeDict)

print("\nDelete an entry\ndel gradeDict['David']\nprint(gradeDict)")
del gradeDict['David']
print(gradeDict)

print("\nEntry can have multiple values\nprint(gradeDict2)")
gradeDict2 = { 'Kelly':[89,88],
               'Jack':[95,87],
               'Samantha':[78,89],
               'Jesse':[92,100],
             }
print(gradeDict2)

print("\nprint(gradeDict2['Jesse'])")
print(gradeDict2['Jesse'])

print("\nScore on the 1st test\nprint(gradeDict2['Jesse'][0])")
print(gradeDict2['Jesse'][0])

print("\n...end of run...")
