# Basic - Print all integers from 0 to 150.

# for x in range(101):
#     print(x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# for x in range(5, 1000, 5):
#     print(x)

# Counting, the Dojo Way - Print integers 1 to 100.
# If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".

x = 0
while x <= 100:
    print(x)
    x += 1
    if x % 10 == 0:
        print("Coding Dojo")
        x += 1
        continue
    if x % 5 == 0:
        print("Coding")
        x += 1
        continue
