n = int(input("ENTER THE NUMBER: "))

reverse= 0

while n > 0:
    digit = n % 10
    n = n // 10
    reverse = reverse * 10 + digit

print(reverse)