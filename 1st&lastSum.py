n= int(input("ENTER THE NUMBER:"))
last = n%10

while n>=10:
    n = n//10

first = n

total =  first+ last
print("THE SUM OF FIRST AND LAST DIGIT IS :", total)