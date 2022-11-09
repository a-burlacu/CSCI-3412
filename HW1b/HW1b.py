########################################################################################################
#                                               PART 1
########################################################################################################
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
with open('output.md', 'a') as f:
    print()
    print("1. The random numbers between 1...1K:  Total guesses:",
          iterator(1, 1000)[0], "Avg:", iterator(1, 1000)[1], file=f)

    print("2. The random numbers between 1...1M:  Total guesses:",
          iterator(1, 1000000)[0], "Avg:", iterator(1, 1000000)[1], file=f)



########################################################################################################
#                                               PART 2
########################################################################################################
"""
Name: Alina Burlacu
ID: 109129252
Date: 09/14/2022
Assignment: HW1b - Part 2 - Simple Time Efficiency Function
Description: A program that takes two input arguments (a function, listPrimeNumbers() and its arguments)
            and returns the start time, end time and time taken to execute the function.
            The test function, listPrimeNumbers(), takes an integer (theMaxNum) and lists all prime numbers
            between 0 and theMaxNum.
            The output is written to a markdown file consisting of: start time, end time, execution time
"""
import timeit


def timeEfficiency(funcName, *args):

    # get start time, perform function execution, get end time
    start = timeit.default_timer()

    primes = listPrimeNumbers(theMaxNum)

    end = timeit.default_timer()

    # calculate the time efficiency
    execution = (end-start)
    # display output in markdown file
    with open('output.md', 'a') as f:
        print()
        print(f"List of prime numbers of {theMaxNum}: {{ 'start': {start:05f},'end': {end:05f}, "
              f"'time efficiency': {execution:05f},\n 'result': {primes}}}", file=f)

# test function to find list of prime numbers given user input
def listPrimeNumbers(num):
    primesList = []
    for i in range(0, num):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                primesList.append(i)
    return primesList

# test driver
theMaxNum = int(input("Enter a number for the list of prime numbers: "))
timeEfficiency(listPrimeNumbers(theMaxNum), theMaxNum)


########################################################################################################
#                                               PART 3
########################################################################################################
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
from random import seed

seed(1)

x = 10000

maxG = -1
minG = 1000000

correct = 0

for i in range(x):

    a = randint(0,9)
    b = randint(0,9)
    c = randint(0,9)

    guessing = True
    num_guesses = 0

    # guessing the triplet in loop until we get correct guess or number of guesses are less than 10000
    while guessing and num_guesses<10000:
        guess_a = randint(0, 9)
        guess_b = randint(0, 9)
        guess_c = randint(0, 9)

        # increment number of guesses by 1
        num_guesses += 1

        if guess_a==a and guess_b==b and guess_c==c:
            guessing = False


    if not guessing:
        correct += 1

    if num_guesses < minG:
        minG = num_guesses

    if num_guesses > maxG:
        maxG = num_guesses

    avg = sum(num_guesses)/len(num_guesses)



# display output in markdown file
with open('output.md', 'a') as f:
    print()
    print("Number of tries: ", x, file=f)
    print("The highest number of guesses in a try: ", maxG,file=f)
    print("The lowest number of tries: ", minG, file=f)
    print("The average number of tries: ", avg, file=f)

########################################################################################################
#                                               PART 4
########################################################################################################
"""
Name: Alina Burlacu
ID: 109129252
Date: 09/14/2022
Assignment: HW1b - Part 4 -  Top 'n' number of words
Description: A program that takes a text file and an integer 'n'  and displays the top ‘n’
            number of words in descending order of its occurrences (case-insensitive) in the file.
"""
def numWords(filename):

    with open(filename, "r") as f:
        l = []
        for line in f.readlines():
            line = line.strip()
            line = line.split()
            for i in line:
                l.append(i.lower())
        d = {}
        for i in l:
            d[i] = l.count(i)

    return d



fname = input("Enter a file name: ")
freq = numWords(fname)

sorted_dict = sorted(freq.items(), key = lambda kv:kv[1], reverse = True)

with open('output.md', 'a') as f:
    print()
    print(fname + ":", file=f)
    for(word,freq) in sorted_dict[:10]:
        print(word + " : ", str(freq), file=f)
