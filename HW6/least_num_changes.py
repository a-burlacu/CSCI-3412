"""
Name: Alina Burlacu
ID: 109129252
Date: 12/09/2022
Assignment: HW6 - Q2 -  The minimum number of changes
Description: Write a Python program to give changes for the minimum number of bills and coins.
            Assume the denominations are $100, $50, $20, $10, $5, $1, 50¢, 25¢, 10¢, 5¢, and 1¢.
            And, there are enough of each to make any required change.

            Specify a change in the conditions above that make this greedy algorithm fail_algorithm.
            Also, show an example that demonstrates the failure.

            Write another Python program to count the total number of ways to give change for any specified amount.
"""


# -------------------------------------------------------------
#        function to compute number of bills and coins
# -------------------------------------------------------------
def change_amount(dollar_amt):

    denominator = [100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.5, 0.01]
    leftovers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_money = 0.00

    for i in range(len(leftovers)):
        while dollar_amt >= zero_money:
            if (zero_money + denominator[i]) <= dollar_amt:
                zero_money += denominator[i]
                leftovers[i] += 1
            else:
                break
        if zero_money == dollar_amt:
            break

    with open('output_least_num_changes.md', 'a') as f:
        print("\n----------------------Correct Returned Amount------------------------\n", file=f)
        for i in range(len(leftovers)):
            print(f"$ {str(denominator[i])}: {str(leftovers[i])}    ", file=f)


# -------------------------------------------------------------
#      function to demonstrate greedy algorithm failure
# -------------------------------------------------------------
def fail_algorithm(dollar_amt):

    dollars_100 = 0
    dollars_50 = 0
    dollars_20 = 0
    dollars_10 = 0
    dollars_5 = 0
    dollars_1 = 0
    cents_50 = 0
    cents_25 = 0
    cents_10 = 0
    cents_5 = 0
    cents_1 = 0

    if dollar_amt <= 0:
        with open('output_least_num_changes.md', 'a') as f:
            print('no change', file=f)
    else:
        dollars_20 = dollar_amt // 20
        dollar_amt %= 20

        dollars_10 = dollar_amt // 10
        dollar_amt %= 10

        dollars_5 = dollar_amt // 5
        dollar_amt %= 5

        dollars_1 = dollar_amt // 1
        dollar_amt %= 1

        dollars_100 = dollar_amt // 100
        dollar_amt %= 100

        dollars_50 = dollar_amt // 50
        dollar_amt %= 50

        # breaking down the change here
        cents_5 = dollar_amt // .05
        dollar_amt %= .05

        cents_50 = dollar_amt // 0.5
        dollar_amt %= .5

        cents_25 = dollar_amt // .25
        dollar_amt %= .25

        cents_10 = dollar_amt // .10
        dollar_amt %= .10

        cents_1 = dollar_amt

    with open('output_least_num_changes.md', 'a') as f:
        print("\n----------Failure of Greedy Algorithm Demonstration----------\n", file=f)
        print(f"$100: {int(dollars_100)}    ", file=f)
        print(f"$50:  {int(dollars_50)}    ", file=f)
        print(f"20: {int(dollars_20)}    ", file=f)
        print(f"$10: {int(dollars_10)}   ", file=f)
        print(f"$5: {int(dollars_5)}   ", file=f)
        print(f"$1: {int(dollars_1)}   ", file=f)
        print(f"$0.50: {int(cents_50)}   ", file=f)
        print(f"$0.25: {int(cents_25)}   ", file=f)
        print(f"$0.10: {int(cents_10)}   ", file=f)
        print(f"$0.05: {int(cents_5)}   ", file=f)
        print(f"$0.01: {int(round(cents_1, 2))}   ", file=f)



# -------------------------------------------------------------
#       function to count number of ways to give change
# -------------------------------------------------------------
def num_of_ways(n):
    denominator = [100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.5, 0.01]
    ways = [0] * (n + 1)
    ways[0] = 1

    # Go through all the money denominations
    for i in range(len(denominator)):

        # Compare each index value
        for j in range(len(ways)):
            if denominator[i] <= j:
                # Update array
                ways[j] += ways[int(j - denominator[i])]

    # return the value at the nth position of array
    return ways[n]


# -------------------------------------------------------------
#                      Driver Code
# -------------------------------------------------------------
if __name__ == "__main__":
    dollar_amt = eval(input("Enter dollar amount to break down into change: "))
    change_amount(dollar_amt)
    fail_algorithm(dollar_amt)

    with open('output_least_num_changes.md', 'a') as f:
        print("\nNumber of ways to return change for specified amount:", num_of_ways(11), file=f)
