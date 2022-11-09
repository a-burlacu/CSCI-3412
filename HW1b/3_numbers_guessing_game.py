"""
Name: Alina Burlacu
ID: 109129252
Date: 09/14/2022
Assignment: HW1b - Part 3 -  3 Number Guessing Game (Randomized vs. Brute-force Algorithms)
Description: A program that generates 3 random integers between [0,9] in a specific order
            then uses 1)Deterministic brute-force algorithm and 2)Pure random algorithm to guess
            the 3 random numbers. It will compute the average number of guesses per try from x
            number of tries, where x >= 10,000
"""
from random import randint


def pureRandom(one,two,three):
    count = 0
    maxG = -1
    minG = 10000

    for i in range(1000):

        guess_a = randint(0, 9)
        guess_b = randint(0, 9)
        guess_c = randint(0, 9)

        count += 1

        if guess_a==one and guess_b==two and guess_c==three:
            count += 1
            break

        if count < minG:
            minG = count

        if count > maxG:
            maxG = count
    return count, minG, maxG



def iterator():
    # initialize list for storing number of guesses each iteration
    guesses = []
    for i in range(0, 1000):  # repeat the guessing game 10,000 times
         # randomly generates 3 number between 0-9
        a = randint(0,9)
        b = randint(0,9)
        c = randint(0,9)


        result = bruteForce(a,b,c)
        low = result[1]
        high = result[2]
        guesses.append(result[0])

    total = sum(guesses)
    average = total / len(guesses)


    # return the total number of guesses and the average number of guesses
    return total, average, high, low




# display output in markdown file
with open('3_number_guessing_game_output.md', 'w') as f:
    print("Number of tries: ", iterator()[0], file=f)
    print("The highest number of guesses in a try: ", iterator()[2],file=f)
    print("The lowest number of tries: ", iterator()[3], file=f)
    print("The average number of tries: ", iterator()[1],file=f)


# from random import sample
# from itertools import permutations
#
#
# def bruteForce(nums):
#     count = 0
#     for i in range(0,100):
#         # find a set of 3 random numbers
#         guess_list = sample(range(0, 10), 3)
#         # find all possible permutations of the set
#         perm_list = list(permutations(guess_list))
#
#         counter = 0
#         for j in range(0,6):
#             if counter == 5:
#                 break
#             if nums == perm_list[j]:
#                 count += 1
#                 break
#             else:
#                 count += 1
#         else:
#             continue
#         break
#
#     return count
#
#
# def pureRandom(nums):
#
#     count = 0
#     for i in range(0,100):
#
#         guess_list = sample(range(0,10),3)
#
#         for j in range(0,100):
#
#             if nums == guess_list:
#                 count += 1
#                 break
#             else:
#                 count += 1
#                 continue
#         else:
#             continue
#         break
#
#     return count
#
#
#
#
#
#
#     # check if 1st order matches
#     # if not, shuffle numbers in a new order
#     # check if 2nd order matches, repeat first steps
#     # increment counter by 1 each time an order is guessed (6 possible times for set of 3)
#
#
#
# def numbersGenerator():
#     guesses = []
#
#     for i in range(0,100):
#
#         rand = sample(range(0,10),3)  #generates 3 random numbers from 0-9 inclusive
#
#         result = pureRandom(rand)
#         guesses.append(result)
#     print(guesses)
#     return guesses
#
#         # call guessing funcitons
#
#
# numbersGenerator()