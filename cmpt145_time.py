# CMPT 145: Computational Complexity
# Defines a get_time() function for use in the lab
#
# get_time()
#   Time can be measured three ways:
#   - how much time has passed?
#   - how many CPU clock cycles have passed?
#   - how many CPU clock cycles were spent on this application?
#   The decision about which of these to use is found in the get_time() function below.

# if you are on a Windows system, you may need to change the defaul
# See lab slides for advice!

import time as time

def get_time():
    """
    This function allows us to make use of several of Python's tools for
    measuring time.  

    :return: The "current" time, as measured by one of Python's time functions.
             The value returned is relative, useful for comparisons, but not
             always interpretable as a time.
    """
    # return time.time()             # wall clock time
    # return timeit.default_timer()  # needs import timeit
    return time.perf_counter()     # counts CPU clock cycles system-wide
    # return time.process_time()       # time spent on this process only

