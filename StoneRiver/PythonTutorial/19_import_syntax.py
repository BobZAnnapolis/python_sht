## import statistics as s
## from statistics import mean
from statistics import mean as m

print("\n19: Import Syntax")
print("=================\n")

## define functions
## ####################################
def separator():
    print("\n\n## ##################################################")

## ####################################

separator()

print("when importing modules, you have to specify the full path of the module name and the "
      "function you are using. this can get tedious. There are shortcuts.")
print("\t1.import statistics as s <- then just use s.fcn")
print("\t2.from statistics import mean <- just reference mean()")

separator()

exList = [5,6,2,1,6,7,2,2,7,4,7,7,7]

print("LONG WAY:\n"
      "import statistics\n"
      "exList = [5,6,2,1,6,7,2,2,7,4,7,7,7]\n"
      "print(statistics.mean(exList))")
## print(s.mean(exList))

print("\nOPTIONAL WAY:\n"
      "import statistics as s\n"
      "print(s.mean(exList))")
## print(s.mean(exList))

print("\nOPTIONAL WAY:\n"
      "from statistics import mean\n"
      "print(mean(exList))")
## print(mean(exList))

print("\nOPTIONAL WAY:\n"
      "from statistics import mean as m\n"
      "print(m(exList))")
print(m(exList))

print("\nOTHER OPTIONS:\n"
      "from statistics import mean, stdev <- can just rev these 2 fcns\n"
      "from statistics import mean as m, stdev as s <- can just rev these 2 fcns as m. and s.\n"
      "from statistics import * <- can just rev the fcns w/o prefix\n"
      "")

separator()
