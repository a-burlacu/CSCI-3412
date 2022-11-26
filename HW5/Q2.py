"""
Name: Alina Burlacu
ID: 109129252
Date: 11/21/2022
Assignment: HW5 - Q2
Description: Python programs implementing Levenshtein Edit Distance (ED) naïve recursive, Memoization DP, and bottom-up versions.
            Then write a driver program that reads all the numbers in the "rand1000.txt"  file as strings.
            For each string ("0" - "999999") in the file, run all three Edit distance programs against the "012345678" (without 9) string
            Using your timeEfficiency() function from HW2, measure the time efficiency of three versions for computing ED of 250K  integer strings
"""
import time

# ------------------------------------------------------------
#            Naïve Recursive Dynamic Programming
# ------------------------------------------------------------
def editDistRec(str1, str2, m, n):  # m = length of str 1, n = length of str2
    # If empty, return the length of the other string
    if m == 0: return n
    if n == 0: return m
    if str1[m - 1] == str2[n - 1]:

        return editDistRec(str1, str2, m - 1, n - 1)

    return 1 + min(editDistRec(str1, str2, m, n - 1),  # insert
                   editDistRec(str1, str2, m - 1, n),  # delete
                   editDistRec(str1, str2, m - 1, n - 1))  # replace


# ------------------------------------------------------------
#                      Memoization DP
# ------------------------------------------------------------
def editDistMemo(str1, str2, m, n, dp):
    if m == 0 or n == 0: return 0
    # if the same state has already been computed
    if dp[m - 1][n - 1] != -1: return dp[m - 1][n - 1]
    # if equal, then we store the value of the function call
    if str1[m - 1] == str2[n - 1]:
        # store it in array to avoid further repetitive work in future function calls
        dp[m - 1][n - 1] = 1 + editDistMemo(str1, str2, m - 1, n - 1, dp)
        return dp[m - 1][n - 1]
    else:
        dp[m - 1][n - 1] = max(editDistMemo(str1, str2, m, n - 1, dp), editDistMemo(str1, str2, m - 1, n, dp))
        return dp[m - 1][n - 1]


# ------------------------------------------------------------
#                       Bottom-up DP
# ------------------------------------------------------------
def editDistBotUp(str1, str2):  # using a dictionary table
    m = len(str1) + 1
    n = len(str2) + 1
    tbl = {}
    for i in range(m): tbl[i, 0] = i  # initialization
    for j in range(n): tbl[0, j] = j  # initialization
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1  # the same or not
            tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost)
    return tbl[i, j]


# ------------------------------------------------------------
#       Function to test time efficiency of algorithms
# ------------------------------------------------------------
def timeEfficiency(func, *args):
    fname = str(args[0])
    # get start time, perform function execution, get end time
    start = time.perf_counter()

    # calls mergeHeap function

    # mergeSort(sorted_list)

    end = time.perf_counter()

    # calculate the time efficiency
    elapsed = (end - start)

    # display output in markdown file
    with open('Q2_output.md', 'a') as f:
        print(
            f'{fname.strip()} algorithm efficiency:  \nstart: {start}  \nend: {end}  \nelapsed time: {elapsed}\n',
            file=f)


# ------------------------------------------------------------
#   Function to open file, read, return list of strings
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
#       Function to iterate over main functions
# ------------------------------------------------------------
def test(check_str, str_list, *args):
    for string in str_list:
        m = len(check_str)
        n = len(string)
        dp = [[-1 for i in range(n)] for j in range(m)]  # intialization

        """ to test functions, uncomment each in turns """

        editDistRec(check_str, string, m, n)
        # editDistMemo(check_str, string, m, n, dp)
        # editDistBotUp(check_str,string)


# ------------------------------------------------------------
#                        Driver code
# ------------------------------------------------------------
def main():
    filename = "rand1000.txt"
    # filename = "rand250000.txt"
    str_list = getIntegers(filename)
    check_str = "012345678"

    """ to test functions, uncomment each in turns """

    timeEfficiency(test(check_str, str_list), "Naïve Recursive")
    # timeEfficiency(test(check_str, str_list), "Memoization DP")
    # timeEfficiency(test(check_str, str_list), "Bottom-up DP")



if __name__ == '__main__':
    main()