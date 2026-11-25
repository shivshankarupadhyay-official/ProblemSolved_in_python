n = int(input("Enter the number: "))

largest_digit = 0

while n>0:
    digit = n %10

    if digit > largest_digit:
        largest_digit = digit

    n  = n//10
print("THE LARGEST DIGIT IS : ", largest_digit)