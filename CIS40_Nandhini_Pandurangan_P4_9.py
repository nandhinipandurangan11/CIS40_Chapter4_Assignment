# CIS40: Summer 2020: Chapter 4 Assignment: Problem 9 : Nandhini Pandurangan
# This program reads a string and prints the string in reverse.


# print_reverse() reads user input and prints it in reverse
def print_reverse():
    string = input("Please enter a word: ").strip()

    for i in range(len(string) - 1, -1, -1): # iterate in reverse
        print(string[i], end="")             # print string in reverse


print_reverse()

'''
Output: 

Please enter a word: harry
yrrah 
----------------------------
Please enter a word: She sells seashells by the seashore
erohsaes eht yb sllehsaes slles ehS
-----------------------------
Please enter a word: 123456789
987654321

'''