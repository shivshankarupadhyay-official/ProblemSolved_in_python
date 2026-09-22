amount = int(input("ENTER THE AMOUNT: "))

if amount > 5000:
    discount = amount * 20 / 100
    print(f"YOU GOT 20% DISCOUNT of {discount} rupees")
elif amount >= 2000:
    discount = amount * 10 / 100
    print(f"YOU GOT 10% DISCOUNT of {discount} rupees")
else:
    discount = 0
    print("NO DISCOUNT!")

final_price = amount - discount
print("FINAL PRICE:", final_price)