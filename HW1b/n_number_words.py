"""
Name: Alina Burlacu
ID: 109129252
Date: 09/14/2022
Assignment: HW1b - Part 4 -  Top 'n' number of words
Description: A program that takes a text file and an integer 'n'  and displays the top ‘n’
            number of words in descending order of its occurrences (case-insensitive) in the file.
"""
def numWords(filename):

    with open(filename, "r") as f:
        l = []
        for line in f.readlines():
            line = line.strip()
            line = line.split()
            for i in line:
                l.append(i.lower())
        d = {}
        for i in l:
            d[i] = l.count(i)

    return d



fname = input("Enter a file name: ")
freq = numWords(fname)

sorted_dict = sorted(freq.items(), key = lambda kv:kv[1], reverse = True)

with open('n_number_words_output.md', 'a') as f:
    print(fname + ":", file=f)
    for(word,freq) in sorted_dict[:10]:
        print(word + " : ", str(freq), file=f)
