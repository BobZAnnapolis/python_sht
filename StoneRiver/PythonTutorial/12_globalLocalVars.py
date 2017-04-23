

print("\n12: Global and Local Variables")
print("==============================\n")

x = 6

## define the functions

## ####################################

def printLocalVar():
    z = 5
    print("fcn_1 : Local var z=5; print(z)",z)

## ####################################

def printLocalGlobalVar():
    z = 7
    print("fcn_2 : Local var z=7; global var x=6; print(z,x)",z,x)

## ####################################

def cannotChangeGlobalVar():
    print("\nCan access global vars inside functions but cannot modify them")
    y = x
    y += 1
    print("fcn_3 : y=x;y += 1; print(y,x)",y,x)

## ####################################

def changeGlobalVar():
    print("\nUse global statement to modify a global var")
    global x
    x += 1
    print("fcn_4 : global x; x += 1; print(x)",x)

## ####################################

def globalBestPractice():
    y = x
    y += 1
    ## print("fcn_4 : global x; x += 1; print(x)",x)
    return y

## ####################################
##
# ## CALL YOUR FUNCTIONS
##
## ####################################

print("Starting X :",x)
printLocalVar()
printLocalGlobalVar()
cannotChangeGlobalVar()
changeGlobalVar()
print("\nx at this point :",x)
print("\nBest Practice : Assign local var to global var; modify local, return local, assign returned val to global; access global")
print("print x :",x)
x = globalBestPractice()
print("x = globalBestPractice(); print x :",x)
