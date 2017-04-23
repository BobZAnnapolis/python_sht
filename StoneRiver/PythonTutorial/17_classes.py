

print("\n17: Classes")
print("===========\n")

## define functions
## ####################################
def separator():
    print("\n\n## ##################################################")

## ####################################

separator()

class calc:
    def add(x,y):
        print("answer =",x," + ",y," = ",(x+y))

    def sub(x,y):
        print("answer =",x," - ",y," = ",(x-y))

    def mult(x,y):
        print("answer =",x," * ",y," = ",(x*y))

    def div(x,y):
        print("answer =",x," / ",y," = ",(x/y))

calc.add(9,4)
calc.sub(9,4)
calc.mult(9,4)
calc.div(9,4)
