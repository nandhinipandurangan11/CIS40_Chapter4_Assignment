# CIS40: Summer 2020: Chapter 4 Assignment: Problem 12 : Nandhini Pandurangan
# This program reads a word and prints all substrings, sorted by length.


# print_substrings() reads user input and prints the substrings
def print_substrings():
    string = input("Please enter a word: ")

    # input validation
    if len(string) == 0:
        print("Cannot print substrings of an empty string!")

    for i in range(len(string) + 1):  # controls the start of the substring
        for j in range(len(string) - i + 1):  # controls end of substring and subsequently sorts by length
            k = i + j  # k controls length of substring

            for p in range (j, k): # printing out the substring
                # print(j,k, end ="")
                print(string[p], end=" ")
            if j < k:
                print()


print_substrings()

'''
Output: 
Please enter a word: rum
r 
u 
m 
r u 
u m 
r u m 
-------------------------------------------
Please enter a word: 
Cannot print substrings of an empty string!
--------------------------------------------
Please enter a word: Python
P 
y 
t 
h 
o 
n 
P y 
y t 
t h 
h o 
o n 
P y t 
y t h 
t h o 
h o n 
P y t h 
y t h o 
t h o n 
P y t h o 
y t h o n 
P y t h o n
'''
