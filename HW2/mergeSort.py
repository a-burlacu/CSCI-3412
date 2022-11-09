"""
Name: Alina Burlacu
ID: 109129252
Date: 09/27/2022
Assignment: HW2 - Part 2 - Merge Sort Algorithm
Description: Using time_efficiency() function, measure the execution time for merge sort
            using two files with 1,000 or 1,000,000 integers
"""
import timeit


def timeEfficiency(funcName, *args):
    fname = args
    # get start time, perform function execution, get end time
    start = timeit.default_timer()

    mergeSort(int_list)

    end = timeit.default_timer()

    # calculate the time efficiency
    execution = (end - start)

    # display output in markdown file
    with open('merge_sort_output.md', 'a') as f:
        print(f"Merge sort efficiency for {fname} integers: {{ 'start': {start:05f},'end': {end:05f}, "
              f"'time efficiency': {execution:05f},\n}}", file=f)


def mergeSort(alist):
    if len(alist) > 1:

        # dividing step
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # merging two halves at each step
        i = 0;
        j = 0;
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        # Handling left-overs
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return alist



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




int_list= getIntegers("rand1000.txt")
timeEfficiency(mergeSort(int_list),"1,000")



int_list = getIntegers("rand1000000.txt")
timeEfficiency(mergeSort(int_list),"1,000,000")