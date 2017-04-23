
print("\n09: IF-ELIF-ELSE examples")
print("===========================\n")

x = 3
y = 7
z = 10
print("x=3; y=7; z=10\n")

print("ELIF executes up until the 1st IF becomes true\n")

if x > y or x < z:
    print(x,'is > than',y,'or less than',z)
elif x < z:
    print(x,'is < than',z)
elif y < z:
    print(y,'is < than',z)
else:
    print('nothing was the case')
