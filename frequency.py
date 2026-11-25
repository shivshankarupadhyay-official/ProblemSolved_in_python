n= int(input("ENTER THE NUMBER:  "))
target = int(input("Enter the digit: "))
count = 0
while n>0:
    digit = n%10

    if digit == target:
        count +=1

    n = n//10


print("Digit appears ",count, "times.")