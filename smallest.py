n = int(input("Enter the number: "))

smallest_digit = 9

while n>0:
    digit = n %10

    if digit < smallest_digit:
        smallest_digit = digit

    n  = n//10
print("THE Smallest  DIGIT IS : ", smallest_digit)