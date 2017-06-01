def main():
    a_seat_count = eval(input("How many Class A seats tickets were sold? "))
    b_seat_count = eval(input("How many Class B seats tickets were sold? "))
    c_seat_count = eval(input("How many Class C seats tickets were sold? "))

    total_ticket_sales(a_seat_count, b_seat_count, c_seat_count)



def total_ticket_sales(a, b, c):
    class_a_seats_cost = 20
    class_b_seats_cost = 15
    class_c_seats_cost = 10

    total_a_revenue = a * class_a_seats_cost
    total_b_revenue = b * class_b_seats_cost
    total_c_revenue = c * class_c_seats_cost

    print('\nTotal revenue from Class A seat sales: ${:0,.0f}'.format(total_a_revenue))
    print('Total revenue from Class B seat sales: ${:0,.0f}'.format(total_b_revenue))
    print('Total revenue from Class C seat sales: ${:0,.0f}'.format(total_c_revenue))
    print('Total revenue from all seat sales: ${:0,.0f}'.format(total_a_revenue + total_b_revenue + total_c_revenue))

main()