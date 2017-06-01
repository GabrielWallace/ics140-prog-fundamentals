TAX_RATE = 0.07
item1 = float(input("Please enter the price (before tax) of the 1st item: "))
item2 = float(input("Please enter the price (before tax) of the 2nd item: "))
item3 = float(input("Please enter the price (before tax) of the 3rd item: "))
item4 = float(input("Please enter the price (before tax) of the 4th item: "))
item5 = float(input("Please enter the price (before tax) of the 5th item: "))

subtotal = item1+item2+item3+item4+item5
tax = subtotal * TAX_RATE
total = subtotal + tax

print("Price before tax is:", subtotal)
print("Price after tax is:", total)

