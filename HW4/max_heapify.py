"""
Name: Alina Burlacu
ID: 109129252
Date: 11/04/2022
Assignment: HW4 - Q5 - max_heapify() using iteration
Description: Modifying max_heapify to use iteration instead of recursion to improve time efficiency

"""
import time
from random import randint


# ------------------------------------------------------------
#                RECURSIVE max_heapify function
# ------------------------------------------------------------
def max_heapify_recur(array, i):
    left = 2 * i
    right = 2 * i + 1
    length = len(array) - 1  # for termination condition check
    largest = i

    if left <= length and array[i] < array[left]:
        largest = left
    if right <= length and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify_recur(array, largest)
    return array


# ------------------------------------------------------------
#                ITERATIVE max_heapify function
# ------------------------------------------------------------
def max_heapify_iter(array, i):
    length = len(array) - 1
    while i <= length:
        left = 2 * i
        right = 2 * i + 1
        largest = i

        if left <= length and array[i] < array[left]:
            largest = left
        if right <= length and array[largest] < array[right]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            max_heapify_iter(array, largest)
        else:
            break
    return array


# ------------------------------------------------------------
#                Function to build max heap
# ------------------------------------------------------------

def build_max_heap(array):
    for i in reversed(range(len(nums) // 2)):
        # max_heapify_iter(array, i)

        # try using recursive version to see difference in time efficiency
        max_heapify_recur(array, i)


# ------------------------------------------------------------
#       Function to test time efficiency of algorithms
# ------------------------------------------------------------
def timeEfficiency(func, *args):
    # get start time, perform function execution, get end time
    start = time.perf_counter()

    # uncomment either function to test time efficiency
    # max_heapify_iter(nums,i)
    max_heapify_recur(nums, i)

    end = time.perf_counter()

    # calculate the time efficiency
    elapsed = (end - start)

    return elapsed


# ------------------------------------------------------------
#                        Driver code
# ------------------------------------------------------------

nums = []  # create a random array of 10 integers
for i in range(10):
    nums.append(randint(-50, 50))

with open('output_max_heapify.md', 'a') as f:
    # uncomment to use with iterative version of max_heapify
    # print(f"### Max_heapify: ITERATIVE\n\nUnsorted array: {nums}           ", file=f)
    # time = timeEfficiency(build_max_heap(nums))
    # print(f"Time Elapsed: {time}           ", file=f)

    # uncomment to use with recursive version of max_heapify
    print(f"### Max_heapify: RECURSIVE\n\nUnsorted array: {nums}           ", file=f)
    time = timeEfficiency(build_max_heap(nums))
    print(f"Time Elapsed: {time}           ", file=f)

    print(f"Sorted array: {nums}\n---\n", file=f)
