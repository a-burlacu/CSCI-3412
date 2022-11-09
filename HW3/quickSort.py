"""
Name: Alina Burlacu
ID: 109129252
Date: 10/14/2022
Assignment: HW3 - Part 3 - Quick Sort Algorithm
Description: Testing the Quick Sort algorithm on its own to verify it works
"""
import timeit
from random import randint


# To test time efficiency of QuickSort
def timeEfficiency(funcName, *args):
    # get start time, perform function execution, get end time
    start = timeit.default_timer()

    quickSort(nums, 0, len(nums) - 1)

    end = timeit.default_timer()

    # calculate the time efficiency
    execution = timeit.timeit(stmt='quickSort(nums,0,len(nums)-1)', globals=globals(), number=5)

    with open('Q3.md', 'a') as f:
        print(f"\nQuickSort efficiency for 20 integers  {{       \nstart: {start:05f}   \nend: {end:05f}   "
              f"\ntime efficiency: {execution:05f}}}         ", file=f)


# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


# Driver code for testing functionality of BubbleSort
nums = []
for i in range(20):
    nums.append(randint(-50, 50))

with open('Q3.md', 'a') as f:
    print(f"Unsorted array: {nums}           ", file=f)
    timeEfficiency(quickSort(nums, 0, len(nums) - 1))
    print(f"Sorted array: {nums}", file=f)
