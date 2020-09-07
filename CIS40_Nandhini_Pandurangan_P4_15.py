# CIS40: Summer 2020: Chapter 4 Assignment: Problem 15 : Nandhini Pandurangan
# This program prompts the user for an integer n
# and prints the nth Fibonacci number


# print_fibonacci() handles user input and printing
def print_fibonacci():
    flag = True
    n = 0

    # input validation
    while flag:
        try:
            n = int(input("Please enter a positive integer: "))

            if n <= 0:
                print("\n ERROR: input must be a positive integer! \n")
                continue

            flag = False
        except:
            print("\n Please enter a valid integer! \n")

    fold1 = 1  # represents trailing #
    fold2 = 1  # represents the # in front of trailing number
    foldnew = 0  # represents current sum

    # input evaluation
    if n == 1:
        print("The 1st number of the Fibonacci Sequence is", fold1)
    elif n == 2:
        print("The 2nd number of the Fibonacci Sequence is", fold1)
    else:
        # this for loop calculates from the 3rd # in the sequence onwards
        for i in range(n - 2):
            foldnew = fold1 + fold2
            fold1 = fold2
            fold2 = foldnew

        # printing the results
        print("The {0}th number in the Fibonacci sequence is {1}".format(n, foldnew))


# calling the function print_fibonacci()
print_fibonacci()

'''
Output: 

Please enter a positive integer: 9
The 9th number in the Fibonacci sequence is 34

------------------------------------------------
Please enter a positive integer: -19

 ERROR: input must be a positive integer! 

Please enter a positive integer: 0

 ERROR: input must be a positive integer! 

Please enter a positive integer: hello

 Please enter a valid integer! 

Please enter a positive integer: 20
The 20th number in the Fibonacci sequence is 6765

---------------------------------------------------

Please enter a positive integer: 50
The 50th number in the Fibonacci sequence is 12586269025
'''