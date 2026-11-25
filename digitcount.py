n= int(input("ENTER THE NUMBER:"))
count = 0

while n>=0:
    digit = n%10
    n = n//10
    count+=1

print("THE NUMBER OF DIGITS IN THE GIVEN NUMBER IS :", count)