"""
Name: Alina Burlacu
ID: 109129252
Date: 10/14/2022
Assignment: HW3 - Part 3 - Combined Bubble Sort + Quick Sort Algorithm
Description: Using time_efficiency() function, measure time efficiency for QuickBubbleSort using 1,000,000 integers
            to find optimal k value for minimizing time efficiency
"""
import timeit
from random import randint
import sys

# sys.setrecursionlimit(10 ** 6)

# ------------------------------------------------------------
#       Function to test time efficiency of algorithms
# ------------------------------------------------------------
def timeEfficiency(funcName, *args):
    fname = args
    # get start time, perform function execution, get end time
    start = timeit.default_timer()

    # quickBubbleSort(int_list, 0, len(int_list)-1, 10)
    quickBubbleSort(int_list, 10)

    end = timeit.default_timer()

    # calculate the time efficiency
    # execution = timeit.timeit(stmt='quickBubbleSort(int_list, 0, len(int_list)-1, 10)', globals=globals(), number=5)
    execution = timeit.timeit(stmt='quickBubbleSort(int_list,10)', globals=globals(), number=5)

    # display output in markdown file
    with open('output_quickBubbleSort.md', 'a') as f:
        print(
            f"Quick + Bubble Sort efficiency for {fname} integers  {{       \nstart: {start:05f}   \nend: {end:05f}   "
            f"\ntime efficiency: {execution:05f}}}         \n", file=f)


# ------------------------------------------------------------
#                   Bubble Sort algorithm
# ------------------------------------------------------------
def bubbleSort(array):
    inputList = len(array)
    # Check if we should attempt sorting
    if inputList > 1:
        # Outer loop
        for i in range(inputList):
            # Inner loop
            for j in range(inputList - 1, 0, -1):
                # Sort in ascending order
                if array[j] < array[j - 1]:
                    # Swap values using temp
                    temp = array[j]
                    array[j] = array[j - 1]
                    array[j - 1] = temp
    # return sorted list
    return array


# ------------------------------------------------------------
#      Function to determine partition position for array
# ------------------------------------------------------------
def partition(arrayList, start, end):
    pivot_idx = end
    pivot = arrayList[pivot_idx]

    smaller_element = -1
    for i in range(0, pivot_idx):
        if arrayList[i] < pivot:
            smaller_element += 1
            arrayList[smaller_element], arrayList[i] = arrayList[i], arrayList[smaller_element]
            # Place the pivot element in its correct location for splitting
    arrayList[smaller_element + 1], arrayList[pivot_idx] = arrayList[pivot_idx], arrayList[smaller_element + 1]
    # Return the pivot element to main function
    return smaller_element + 1


# ------------------------------------------------------------
#                Quick + Bubble Sort algorithm
# ------------------------------------------------------------


def quickBubbleSort(arrayList, k):
    len_of_list = len(arrayList)
    if len_of_list > k:
        # Get the index of the pivot element to split the list
        pivot_index = partition(arrayList, 0, len_of_list - 1)
        # Split the list using pivot and recurse
        quickBubbleSort(arrayList[:pivot_index - 1], k)
        quickBubbleSort(arrayList[pivot_index + 1:], k)

    return bubbleSort(arrayList)


# ------------------------------------------------------------
#   Function to parse text file for integers to add to array
# ------------------------------------------------------------
def getIntegers(filename):
    with open(filename, "r") as f:
        l = []
        for line in f.readlines():
            line = line.strip()
            line = line.split()
            for i in line:
                l.append(i.lower())

        return l


# ------------------------------------------------------------
#                        Driver code
# ------------------------------------------------------------

# int_list = []
# for i in range(1000):
#     int_list.append(randint(-50, 50))

int_list = getIntegers("rand1000.txt")
timeEfficiency(quickBubbleSort(int_list, 10), "1000")
