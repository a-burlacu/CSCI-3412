"""
Name: Alina Burlacu
ID: 109129252
Date: 11/21/2022
Assignment: HW5 - Q3
Description: Develop a very slow hash function (?) and a hash table of integer strings in the given 250K data file.
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