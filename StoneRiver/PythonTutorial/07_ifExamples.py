
print("\n07: IF examples")
print("===============\n")

x = 2
y = 7
z = 10

print("x=2; y=7, z=10\n")
print('print x if it is greater than y')
if x > y:
    print(x,'is greater than',y)

print('\nprint x if it is less than y')
if x < y:
    print(x,'is less than',y)

print('\nprint x if it is the same as y, equality uses ==')
if x == y:
    print(x,'is the same as',y)

print("\nif x == '2':")
if x == '2':
    print(x,'is the same as 2')

print("\nif x <= y:")
if x <= y:
    print(x,'is less than or equal to',y)

print("\nz is greater than y which is greater than x")
if z > y > x:
    print(z,'is greater than',y,'which is greater than',x)
