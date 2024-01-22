'''i = 3
while i != 0:
    print("meow")
    i = i -1'''

#Using while loop
print("Using while loop")
i = 0
while i < 3:
    print("meow")
    i += 1

#Using for loop
print("\nUsing for loop")
for i in range(3):
    print("meow")

#Another way to print meow
print("\nWithout using any of the loop")
print("meow\n" * 3, end="")