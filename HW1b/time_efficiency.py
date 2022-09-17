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
    with open('time_efficiency_output.md', 'w') as f:
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
