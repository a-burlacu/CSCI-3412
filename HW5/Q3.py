"""
Name: Alina Burlacu
ID: 109129252
Date: 11/21/2022
Assignment: HW5 - Q3
Description: Develop a very slow hash function & hash table of integer strings in the given 250K data file.
            Modify the Edit Distance "recursive" function to count the number of recursive function calls to find the
             minimal Edit Distance between an integer string and "012345678"
            You may consider this recursive function as a very very very slow hash function of integer strings.
            This function will map a given integer string into the index of a (hash) table and the table keeps track of
             the number of collisions for each index instead of storing collided integer strings in its auxiliary linked list.
            Now, for the 250K integer strings in rand250000.txt, you invoke the modified recursive function for
             each integer string, Then record the collision number for the index of each integer string in the table.
            Upon completion, you may observe fairly well uniformly distributed collision numbers in the hash table
             if you print them out. It would be ideal if the average collision number is close to(250,000/hash table size.
            Draw an offline bar graph to show the relationship between hashed indexes
             (the number of recursive calls to compute the Edit Distance of an integer string against "012345678" )
             and the number of collisions for each index to the hash table.

"""
from operator import add
from plotly import graph_objects as go
from plotly import offline
# ------------------------------------------------------------
#                   Helper function
# ------------------------------------------------------------
def process(a, b):
    return a[0] if a[0] > b[0] else b[0], a[1] + b[1]


# ------------------------------------------------------------
#            Naïve Recursive Dynamic Programming
# ------------------------------------------------------------
def editDistRec(str1, str2, m, n):  # m = length of str 1, n = length of str2
    # If empty, return the length of the other string
    if m == 0 or n == 0:
        return 0,1
    elif str1[m - 1] == str2[n - 1]:
        result = editDistRec(str1, str2, m - 1, n - 1)
        return tuple(map(add, result, (1, 1))) if (6000 >= result[1] > 0) else tuple(0, 0)
    else:
        resultA = editDistRec(str1, str2, m , n - 1)
        if resultA[1] > 6000 or resultA[1] == 0:
            return 0, 0
        resultB = editDistRec(str1, str2, m-1 , n)
        if resultB[1] > 6000 or resultB[1] == 0 or resultA[1] + resultB[1] > 6000:
            return 0, 0
        return tuple(map(add, process(resultA, resultB), (0, 1)))


# ------------------------------------------------------------
#               Hash Function & Hash Table Class
# ------------------------------------------------------------
def hash_func(str):
    return abs(hash(str))


class HashTable:
    def __init__(self, size):
        self.table = [0] * size
        self.size = size
        self.collisions = [0] * size

    def insert(self, hash_value, value):
        index = hash_value % self.size
        if self.table[index] != 0:
            self.collisions[index] += 1
        else:
            self.table[index] = value


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
#                        Driver code
# ------------------------------------------------------------
def main():
    # filename = "rand1000.txt"
    filename = "rand250000.txt"
    check_str = "0123456789"

    str_list = getIntegers(filename)
    table = HashTable(10000)

    for num in str_list:
        key = editDistRec(num, check_str, len(num), len(check_str))
        if key[1] == 0:
            table.insert(hash_func(num), num)
        else:
            table.insert(key[1], num)

    fig = go.Figure(data=go.Scatter(y=table.collisions),
                    layout=go.Layout(
                        yaxis=dict(title="Collision size"),
                        xaxis=dict(title="Hash keys")))
    offline.plot(fig,filename='Q3_graph.html')


if __name__ == '__main__':
    main()
