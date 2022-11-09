"""
Name: Alina Burlacu
ID: 109129252
Date: 10/14/2022
Assignment: HW3 - Part 3 - Bubble Sort Algorithm
Description: Testing the Bubble Sort algorithm on its own to verify it works
"""
import timeit
from random import randint


# To test time efficiency of BubbleSort
def timeEfficiency(funcName, *args):
    # get start time, perform function execution, get end time
    start = timeit.default_timer()

    bubbleSort(nums)

    end = timeit.default_timer()

    # calculate the time efficiency
    execution = timeit.timeit(stmt='bubbleSort(nums)', globals=globals(), number=5)
    with open('Q3.md', 'a') as f:
        print(f"\nBubbleSort efficiency for 20 integers  {{       \nstart: {start:05f}   \nend: {end:05f}   "
              f"\ntime efficiency: {execution:05f}}}         ", file=f)


# BubbleSort algorithm
def bubbleSort(array):
    sorted_nums = []
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# Driver code for testing functionality of BubbleSort
nums = []
for i in range(20):
    nums.append(randint(-50, 50))

with open('Q3.md', 'a') as f:
    print(f"Unsorted array: {nums}           ", file=f)
    timeEfficiency(bubbleSort(nums))
    print(f"Sorted array: {nums}", file=f)
