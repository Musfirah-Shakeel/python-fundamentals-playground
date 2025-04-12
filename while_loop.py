# Check even and odd numbers from 1 to 20 using while loop

i = 1

print("Checking Even and Odd numbers from 1 to 20...\n")

while i <= 20:
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
    i += 1

print("\nTask completed successfully!")