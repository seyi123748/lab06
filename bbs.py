# CMPT 145: Computational Complexity
# Defines a sorting function using the infamous bubblesort algorithm
#
# The bubblesort works by swapping values repeatedly.
# if an adjacent pair of values is out of order, swap them
# Keep repeating, until a whole sweep goes by without any swaps
# (at most len(alist) sweeps for this to happen, usually fewer)
#
# The bubblesort is bad for 2 reasons.
# 1. Theoretically, bubblesort has high computational complexity
# 2. Bubblesort uses none of Python's efficient functionality
#


def bubblesort(alist):
    """
    Purpose:
        Sort the given list.
    Preconditions:
        :param alist: a list of values that can be compared, like numbers
    Post-conditions:
        The given list is sorted, in order of increasing values.
    Return:
        :return:  None
    """
    sweep = 0
    swapped = True
    # perform sweeps until no values are swapped
    while sweep < len(alist) and swapped:
        swapped = False
        for j in range(len(alist)-1):
            # check if adjacent values are out of order
            if alist[j] > alist[j+1]:
                # if so, swap them!
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
                swapped = True # remember that a swap occurred
    # that's it!


if __name__ == "__main__":
    # simple test script
    input = []
    output = []
    bubblesort(input)

    if output != input:
        print("Error: bubblesort failed on empty input")

    input = [5]
    output = [5]
    bubblesort(input)

    if output != input:
        print("Error: bubblesort failed on input list of one element")

    input = [1,2,3]
    output = sorted(input)  # returns a sorted copy of the list!
    bubblesort(input)       # sorts the list without making a copy

    if output != input:
        print("Error: bubblesort failed on small sorted input")

    input = [3,2,1]
    output = sorted(input)  # returns a sorted copy of the list!
    bubblesort(input)       # sorts the list without making a copy

    if output != input:
        print("Error: bubblesort failed on small reverse-sorted input")

    input = [9,8,7,1,2,3,4,6,5,7,2,4,8]
    output = sorted(input)  # returns a sorted copy of the list!
    bubblesort(input)       # sorts the list without making a copy

    if output != input:
        print("Error: bubblesort failed on small unsorted list")