
print("\n21: Error Handling - Try and Except")
print("===================================\n")

print("Try a block of code and if an exception occurs, trap it to handle it.")
print("Use 'Exception' to trap ANY exception, can use others.")
print("Format is:\ntry:\n\tcode...\nexcept Exception as e:\n\t..handle exception")
print("\nCan also stack exceptions to look for specific kinds.")
print("\tbut if you use these and an unlisted one happens - program will crash.")
print("try:\n\tcode...\nexcept TypeError as t:\n\t..handle typeError exception")
print("except NameError as n:\n\t..handle nameError exception\n")
print("Get around a crash by including Exception as 1 to handle, eg")
print("try:\n\tcode...\nexcept TypeError as t:\n\t..handle typeError exception")
print("except NameError as n:\n\t..handle nameError exception")
print("except Exception as e:\n\t..handle exception")

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

try:
    print("Running the try...\ntry:\n\tprint('5'+5)")
    print('5'+5)

except Exception as e:
    print("Hitting the exception...\nexcept Exception as e:\n\tprint('\\t',str(e))")
    print("\t",str(e))

print('\nCode continues after exception is handled...if possible...\n')

print("When handling exceptions, usually a good idea to do a Print(str(e)) to understand what went wrong, helps debug.\n")
