n= int(input("ENTER THE NUMBER:"))
reverse = 0
original = n
while n>0:
    digit = n%10
    n= n//10

    reverse = reverse *10 + digit

if reverse == original:
    print("THE NUMBER IS PALINDROME !")

else:
    print("THE NUMBER IS not PALINDROME !")