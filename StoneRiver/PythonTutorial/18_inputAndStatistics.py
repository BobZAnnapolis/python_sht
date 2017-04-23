import statistics

print("\n18: Input and Statistics")
print("========================\n")

## define functions
## ####################################
def separator():
    print("\n\n## ##################################################")

## ####################################

separator()

print("Raw input handling is a built-in function")
print("\tuseful for getting answers and data from the user")

print("\ncalled either input or raw_input depending on Python version")

name = input("\nWhat is your name ?: ")
print("You answered :", name)

separator()

print("\nplaying with the statistics module\n")

print("exList = [5,3,2,8,7,4,3,1,8,9,8]\nx = statistics.mean(exList)\nprint(x)")
exList = [5,3,2,8,7,4,3,1,8,9,8]
x = statistics.mean(exList)
print(x)

print("\nx = statistics.median(exList)\nprint(x)")
x = statistics.median(exList)
print(x)

print("\nx = statistics.mode(exList)\nprint(x), ie, the item that occurs most often")
x= statistics.mode(exList)
print(x)

print("\nx = statistics.stdev(exList)\nprint(x)")
x= statistics.stdev(exList)
print(x)

print("\nx = statistics.variance(exList)\nprint(x)")
x= statistics.variance(exList)
print(x)

separator()
