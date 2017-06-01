bug_count = 0
bug_sum = 0
for i in range(5):
    user_input = eval(input("Enter number of bugs for the day "))
    bug_count = bug_count + user_input
print(bug_count)