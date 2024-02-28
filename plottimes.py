# CMPT 145: Algorithm Analysis
# Defines some empirical experiments to understand computational complexity.
#
# In this script, we run experiments on computation time.
# The experiments use three different computational tasks.
#  - Python's built-in sort() operation
#  - a simple implementation of bubblesort
#  - a simple linear search
# Clearly, the sort() and bubblesort() are doing the same task, and
# the linear search is quite different.
# We can compare the two sort functions to each other, and see that
# bubblesort is worse than Python's sort().
# But it's not just measurably worse, it's a different kind of worse.
# Theoretically, sort() and bubblesort() are in different categories.
# To demonstrate a third category, the linear search is used.
# TL;DR
#   - three different algorithms, each one is a different category
#
# This set of experiments collects the raw time measures.
#
# We take the minimum time seen from a number of trials,
# because we know that random causes will increase the
# amount of time needed; but the experiments below do not
# allow for measurement error in the negative direction!
# (you have to set up the experiment so that this is true)


import Statistics as Stat
import apparatus as apparatus
import matplotlib.pyplot as plt

trials = 10

#
print("Statistics for Python's sort()")
sort_sizes = range(50,501,50)
sort_times = []
for n in sort_sizes:
    t1 = Stat.create()
    for i in range(trials):
        Stat.add(t1,apparatus.run_sort(n))
    rtime = Stat.minimum(t1)
    print(n, rtime)
    sort_times.append(rtime)


print("Statistics for bubblesort()")
bubblesort_sizes = range(50,501,50)
bubblesort_times = []
for n in bubblesort_sizes:
    t1 = Stat.create()
    for i in range(trials):
        Stat.add(t1,apparatus.run_bubblesort(n))
    rtime = Stat.minimum(t1)
    print(n, rtime)
    bubblesort_times.append(rtime)



print('Statistics for find')
linsearch_sizes = range(50,501,50)
linsearch_times = []
for n in linsearch_sizes:
    t1 = Stat.create()
    t2 = Stat.create()
    for i in range(trials):
        Stat.add(t1,apparatus.run_find(n))
    rtime = Stat.minimum(t1)
    print(n, rtime)
    linsearch_times.append(rtime)


print('Data collection done... Plotting graphs!')

# plot the results
# we had 3 experiments, so we need three axes
fig, (ax1, ax2, ax3) = plt.subplots(3)

# put the title on the first
ax1.set(title="Timing curves", ylabel="sort()")
ax1.plot(sort_sizes, sort_times,'o-')

ax2.set(ylabel="Bubblesort")
ax2.plot(bubblesort_sizes, bubblesort_times,'o-')

ax3.set(ylabel="Lin. Search")
ax3.plot(linsearch_sizes, linsearch_times,'o-')

# makes the plot a bit neater
plt.tight_layout()
plt.show()
