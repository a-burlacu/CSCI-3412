"""
Name: Alina Burlacu
ID: 109129252
Date: 09/27/2022
Assignment: HW2 - Part 2 - Insertion Sort algorithm
Description: Using time_efficiency() function, measure the execution time for insertion sort
            using two files with 1,000 or 1,000,000 integers
"""
import timeit


def timeEfficiency(funcName, *args):
    fname = args
    # get start time, perform function execution, get end time
    start = timeit.default_timer()

    insertionSort(int_list)

    end = timeit.default_timer()

    # calculate the time efficiency
    execution = (end - start)

    # display output in markdown file
    with open('insertion_sort_output.md', 'a') as f:
        print(f"Insertion sort efficiency for {fname} integers: {{ 'start': {start:05f},'end': {end:05f}, "
              f"'time efficiency': {execution:05f},\n}}", file=f)


def insertionSort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > current:
            alist[j + 1] = alist[j]
            j -= 1
            alist[j + 1] = current


# function to parse txt file and return list of integers
def getIntegers(filename):
    with open(filename, "r") as f:
        l = []
        for line in f.readlines():
            line = line.strip()
            line = line.split()
            for i in line:
                l.append(i.lower())

        return l


int_list = getIntegers("rand1000.txt")
timeEfficiency(insertionSort(int_list), "1,000")

int_list = getIntegers("rand1000000.txt")
timeEfficiency(insertionSort(int_list), "1,000,000")
