import random

def main():
    random_numbers = random.sample(range(1, 1000), 100)
    count_evens_odds(random_numbers)

def count_evens_odds(num_list):
    even_count = 0
    odd_count = 0

    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(num_list)
    print('The number of even numbers in the list is:', even_count)
    print('The number of even numbers in the list is: ', odd_count)

main()