DISCOUNT = 0.2

priceBeforeDiscount = float(input("Please enter the pre-sale price of the item: "))

discountAmt = priceBeforeDiscount * DISCOUNT
priceAfterDiscount = priceBeforeDiscount - discountAmt

print("The price after discount is: $", priceAfterDiscount)
print("You saved: $", discountAmt)
