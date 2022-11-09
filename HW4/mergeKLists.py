"""
Name: Alina Burlacu
ID: 109129252
Date: 11/04/2022
Assignment: HW4 - Q1 - Merging k sorted lists into one sorted list
Description: Read the integers from rand1000000.txt. Split it into 100 rand10000 lists.
            Sort  50 sublists  with radixSort with countingSort as underlying sort for each digit
            Remaining  50   sublists with bucketSort
            Merge the 100 sorted sublists into one sorted list using the heap-merging algorithm of time O(n*log(k))
"""
import heapq
import time


# ------------------------------------------------------------
#   Function to open file, read, and write to 100 sub-files
# ------------------------------------------------------------
def getIntegers(filename):
    # open initial file 'rand1000000.txt'
    file = open(filename, 'r')
    result = []
    for line in file:
        line = line.strip()
        nums = line.split(" ")
        for word in nums:
            if word.strip():
                result.append(word)

    # putting 10,000 integers in 100 different files
    num_frame = [[0 for i in range(0, 10000)] for j in range(0, 100)]
    outfile = open('lists/sublist0.txt', 'w')
    row = 0  # will be index for example sublist [row]+.txt
    col = 0
    for line in result:
        num_frame[row][col] = int(line)
        outfile.write('%s,' % line)
        col += 1
        if (col % 10000 == 0):  # remainder ==0, we close the file
            outfile.close()
            col = 0
            row += 1
            outfile = open('lists/sublist' + str(row) + '.txt', 'w')
    outfile.close()


# ------------------------------------------------------------
#                        Radix Sort
# ------------------------------------------------------------
def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10

    return arr


# REF: https://www.geeksforgeeks.org/radix-sort/


# ------------------------------------------------------------
#                      Counting Sort
# ------------------------------------------------------------
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# ------------------------------------------------------------
#                      Bucket Sort
# ------------------------------------------------------------
def bucketSort(firstList):
    bucket = []
    slotNum = (max(firstList) - min(firstList) + 1) // len(firstList) + 1
    for i in range(slotNum):
        bucket.append([])
    for j in firstList:
        indexB = (j - min(firstList) + 1) // len(firstList)
        bucket[indexB].append(j)

    for i in range(slotNum):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(slotNum):
        for j in range(len(bucket[i])):
            firstList[k] = bucket[i][j]
            k += 1
    return firstList


# REF: https://www.geeksforgeeks.org/bucket-sort-2/


# ------------------------------------------------------------
#                     Merge-Heap Algorithm
# ------------------------------------------------------------
def mergeHeap(sorted_list):
    result = []  # result list
    heap = []  # setting open list for elements inside the heap
    list_index = 0  # list index

    for list in sorted_list:
        heapq.heappush(heap, (list[0], list_index, 0))  # push first element from lists into our heap
        list_index += 1  # move to next list index
    while heap:
        number, list_index, number_index = heapq.heappop(heap)  # pop significant number from heap into result list
        result.append(number)
        number_index += 1  # going to next index

        if number_index < len(sorted_list[list_index]):  # while we still have remaining numbers, add to heap
            heapq.heappush(heap, (sorted_list[list_index][number_index], list_index, number_index))

    return result


# ------------------------------------------------------------
#           MergeSort algorithm for O(nk) comparison
# ------------------------------------------------------------
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


# ------------------------------------------------------------
#       Function to test time efficiency of algorithms
# ------------------------------------------------------------
def timeEfficiency(func, *args):
    # get start time, perform function execution, get end time
    start = time.perf_counter()

    # calls mergeHeap function
    mergeHeap(sorted_list)

    # mergeSort(sorted_list)

    end = time.perf_counter()

    # calculate the time efficiency
    elapsed = (end - start)

    # display output in markdown file
    with open('efficiency_mergeKLists.md', 'a') as f:
        print(
            f"MergeSort algorithm efficiency: {{       \nstart: {start:05f}   \nend: {end:05f}   "
            f"\nelapsed time: {elapsed:05f}}}         \n", file=f)


# ------------------------------------------------------------
#                        Driver code
# ------------------------------------------------------------
# Call splitting function to create 100 sublists
fileName = "rand1000000.txt"
getIntegers(fileName)

sorted_list = []
# Go through first 50 sublists and perform Bucket Sort
for i in range(0, 50):
    temp_list = []
    file = open('lists/sublist' + str(i) + '.txt', 'r')
    for line in file:
        line = line.strip()
        nums = line.split(",")  # numbers are seperated by ','
        for word in nums:
            if word.strip():
                temp_list.append(int(word))  # add numbers into temp_list
    file.close()

    bucketSort(temp_list)  # perform bucket sort algorithm
    sorted_list.append(temp_list)  # then put our sorted temp_list into our sorted_list

# Go through second set of 50 sublists, and perform Radix Sort
for i in range(50, 100):
    temp_list = []
    file = open('lists/sublist' + str(i) + '.txt', 'r')
    for line in file:
        line = line.strip()
        nums = line.split(",")
        for word in nums:
            if word.strip():
                temp_list.append(int(word))
    file.close()

    radixSort(temp_list)  # perform radix sort
    sorted_list.append(temp_list)

final_list = mergeHeap(sorted_list)

timeEfficiency(mergeHeap(sorted_list), sorted_list)

# timeEfficiency(mergeSort(sorted_list),sorted_list)

with open('output_mergeKLists.md', 'a') as f:
    print(final_list, file=f)
