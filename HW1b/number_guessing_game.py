"""
Name: Alina Burlacu
ID: 109129252
Date: 09/14/2022
Assignment: HW1b - Part 1 - Number Guessing Game (Binary Search)
Description: A program that generates a random integer between 1-1000,
            then uses binary search algorithm to guess the random number.
            Will print output to markdown file after running two instances of the game:
            1. for range 1-1,000 using 10,000 iterations
            2. for range 1-1,000,000 using 10,000 iterations
            Output includes total number of guesses and average number of guesses for each instance
"""
from random import randint


def binarySearch(array, x, low, high):
    count = 0
    # while the range of numbers is valid
    while low <= high:
        mid = (low + high) // 2  # using a floor division by 2, get the midpoint of the numbers list

        if array[mid] < x:  # if x is on right side
            low = mid + 1
            count += 1

        elif array[mid] > x:  # if x is on left side
            high = mid - 1
            count += 1

        else:
            # return the value of the index 'mid' not 'mid' itself, since it will be off by 1
            return count
    return -1


# iterator function to allow for multiple inputs
def iterator(n, m):

    # create list of numbers from n-m(inclusive)
    nums = list(range(n, m + 1))

    # initialize list for storing number of guesses each iteration
    guesses = []
    for i in range(0, 10000):  # repeat the guessing game 10,000 times
        rand = randint(n, m)  # randomly generates a number between 1- 1000

        # call the binary search function
        result = binarySearch(nums, rand, 1, len(nums) - 1)
        guesses.append(result)

    total = sum(guesses)
    average = total / len(guesses)

    # return the total number of guesses and the average number of guesses
    return total, average


# display output in markdown file
with open('guessing_game_output.md', 'w') as f:
    print("1. The random numbers between 1...1K:  Total guesses:",
          iterator(1, 1000)[0], "Avg:", iterator(1, 1000)[1], file=f)

    print("2. The random numbers between 1...1M:  Total guesses:",
          iterator(1, 1000000)[0], "Avg:", iterator(1, 1000000)[1], file=f)
