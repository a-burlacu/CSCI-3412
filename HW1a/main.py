s1 = input("enter first string: ")
s2 = input("enter second string: ")

# Enter first string into list character by character
list = []
for i in range(len(s1)):
    list.append(s1[i])

# Initialize empty list for second string
list2 = []
# Check if both strings are same length, if not, return Error
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                # For every character in string 1, if it's the same
                # in string 2, append it to the second list
                list2.append(char2)

    # Check both lists are equal,if yes, it is anagram (True)
    # if no, they are not anagrams (False)
    if list == list2:
        print("True")
    else:
        print("False")
else:
    print("Error: strings not the same length")
