## run a block of code until the condition is false

## for loops often used to iterate thru a list

print("\n05: WHILE loops\n")
print("===============\n")

print("\nsingle line comments start with a double # sign\n\nmultiple line comments sart and end with 3 single quote marks\n")

print("\nwhile loop - simple example\n")
condition = 1

while condition < 10:
	print(condition)
	condition += 1

condition = ' '

'''
uncomment the following to have an infinite loop
	infinite lops can be broken via ctrl-c
while True:
	print(condition + 'True')
	condition = condition + " "
'''
