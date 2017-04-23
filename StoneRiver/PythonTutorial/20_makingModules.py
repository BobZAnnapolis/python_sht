import exMod

print("\n20: Making Modules")
print("==================\n")

print("Modules are [usually] self-contained files containing functions dedicated to a singular task.")
print("Modules are imported into other modules to perform these tasks.")

print("\nPython looks in the current dir for imported modules, \installed dir, \lib, \site-packages.")
print("If you get an import error, modules file cannot be found in defined search paths")

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

print('import exMod\nexMod.exampleFunc("This Is A Test")\n')
exMod.exampleFunc("This Is A Test")

separator()

