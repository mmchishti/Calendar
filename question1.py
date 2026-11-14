days = int(input("Enter the number of days: "))

start = int(input("Enter the starting day(1=sun, 2=mon, ..., 7=sat): "))

print("Sun Mon Tue Wed Thu Fri Sat")

print("    " * (start - 1), end="")

for i in range(1, days + 1):
    print(f"{i:>3}", end=" ")
    if (i + start - 1) % 7 == 0:
        print()  # Move to the next line after Saturday 