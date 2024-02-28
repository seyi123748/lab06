# CMPT 145: Algorithm Analysis
# Defines three different versions of a check_range function, similar to Assignment 1
# The question is: which one is more efficient, and why?#



# This version uses a list seen, and records values as they are seen
def versionA(alist):
  """
  Purpose:
    Check that the list contains all the numbers 1 ... N
  Pre-Conditions:
    alist: a list of numbers
  Post-conditions:
    None
  Return:
    True if all the numbers are there
  """
  # seen is a list of booleans, to record values observed in the square
  N = len(alist)
  seen = N*[False]
   
  # check for repeated numbers 
  for i in range(N):
      val = alist[i]
      # has val been seen before?
      if val > 0 and val <= N and not seen[val-1]:
        # no, so we mark it seen now
        seen[val-1] = True
      else:
        # yes, so it must be a repeated number
        return False

  # check that all the numbers were seen.
  for i in range(N):
    if not seen[i]:
      return False

  # no repeats, and all numbers seen
  return True
  

# This version checks the list against a range
def versionB(alist):
  """
  Purpose:
    Check that the list contains all the numbers 1 ... N
  Pre-Conditions:
    alist: a list of numbers
  Post-conditions:
    None
  Return:
    True if all the numbers are there
  """
  # seen is a list of booleans, to record values observed in the square
  N = len(alist)
   
  # check for repeated numbers 
  for i in range(1,N+1):
      if i not in alist:
          return False

  # no repeats, and all numbers seen
  return True
  

# this version sorts the list, and then checks if the list is the same as a range
def versionC(alist):
  """
  Purpose:
    Check that the list contains all the numbers 1 ... N
  Pre-Conditions:
    alist: a list of numbers
  Post-conditions:
    None
  Return:
    True if all the numbers are there
  """
  N = len(alist)
  acopy = [v for v in alist]
  acopy.sort()
  
  if alist == list(range(1,N+1)):
    return True
  else:
    return False
 