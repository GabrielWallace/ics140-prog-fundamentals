def main():
    purchases = eval(input("Enter the number of packages purchased: "))
    discount_calc(purchases)

def discount_calc(n):
    discount = 0
    total_sales_price = n * 99
    if n >= 10 and n <= 19:
        discount = 0.10
    elif n >= 20 and n <= 49:
        discount = 0.20
    elif n >= 50 and n <= 99:
        discount = 0.30
    elif n >= 100:
        discount = 0.40

    if n >=10:
        discount_amount = total_sales_price * discount
        print(discount_amount)

main()