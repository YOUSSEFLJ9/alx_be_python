size = int(input("Enter the size of the pattern: "))

if size > 0:
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("*", end="")
            j += 1
        print("")  # Move to the next line
        i += 1