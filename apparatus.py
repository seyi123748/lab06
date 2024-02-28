# CMPT 145: Computational Complexity
# Defines some functions for experiments to understand computational complexity.
#
# get_time()
#   Time can be measured three ways:
#   - how much time has passed?
#   - how many CPU clock cycles have passed?
#   - how many CPU clock cycles were spent on this application?
#   The decision about which of these to use is found in the get_time() function below.
#
# run_sort()
# run_bubblesort()
# run_find()
#   These functions set up an experiment by creating a random list, and
#   running the function on the list.  The experiments obtain the time
#   just before and just after the function call.  The difference is returned.
#   The time taken does not include the time required to set up the experiment


import random as rand
import cmpt145_time as cmpt145_time
import bbs as bbs


def run_sort(n):
    """
    Purpose:
        Time the execution of Python's built-in sort() operation on lists.
    :param n: The size of the list to sort
    :return: A measure of the time taken.
    """
    numbers = []
    for i in range(n):
        numbers.append(rand.randint(0,n))

    start = cmpt145_time.get_time()
    numbers.sort()
    end = cmpt145_time.get_time()

    return end - start


def run_bubblesort(n):
    """
    Purpose:
        Time the execution of the bubblesort function.
    :param n: The size of the list to sort
    :return: A measure of the time taken.
    """
    numbers = []
    for i in range(n):
        numbers.append(rand.randint(0,n))

    start = cmpt145_time.get_time()
    bbs.bubblesort(numbers)
    end = cmpt145_time.get_time()

    return end - start

def run_find(n):
    """
    Purpose:
        Time the execution of a simple linear search in a list.
    :param n: The size of the list to search
    :return: A measure of the time taken.
    """
    numbers = []
    for i in range(n):
        numbers.append(rand.randint(0,n))

    target = n+2  # the target is not in the list!

    start = cmpt145_time.get_time()
    for n in numbers:
        if target == n:
            break
    end = cmpt145_time.get_time()

    return end - start

