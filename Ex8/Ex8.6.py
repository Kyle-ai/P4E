#write a program that outputs the user for a list of the numbers and prints
#out the maximum and minimum of the numbers at the end when the user enters
#'done'. Write the program to store the numbers the user enters in a list
#and use the max() and min() methods ot compute the maximim and minimum numbers
#after the loop.
def minmax():
    int_num_lst = input("Enter a list of numbers sperated by a space: ")
    user_lst = int_num_lst.split()
    maxnum = 0
    minum = 0
    for i in range(len(user_lst)):
        user_lst[i] = int(user_lst[i])
    maxnum = max(user_lst)
    minum = min(user_lst)
    print("Max num is ", maxnum)
    print("Min num is ", minum)
minmax()
