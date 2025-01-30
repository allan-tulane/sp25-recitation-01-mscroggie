"""
CMPS 2200  Recitation 1
"""
from types import new_class

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
	if right >= left:

		i = (left+right)//2
		if mylist[i] == key:
			return i
		elif mylist[i] > key:
			return _binary_search(mylist, key, left, i-1)
		elif mylist[i] < key:
			return _binary_search(mylist,key, i+1, right)
	else: return -1





	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	start_time = time.time()
	search_fn(mylist, key)
	end_time= time.time()
	runtime = end_time - start_time
	return runtime

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	runtimes=[]

	for size in sizes:
		i = 0
		new_list= []
		while i <= size-1:
			new_list.append(i)
			i+=1
		linear_search_time = time_search(linear_search,new_list,-1)
		binary_search_time = time_search(binary_search,new_list,-1)
		runtimes.append((size,linear_search_time, binary_search_time))
	return runtimes



###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

