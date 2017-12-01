def bsort(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if(arr[i] > arr[j]):
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
	return arr

def qsort(arr):
	if arr:
		head, *tail = arr
		return qsort([x for x in tail if x <= head]) + \
				[head] + \
				qsort([x for x in tail if x > head])
	return []


if __name__ == "__main__":

	import timeit

	print("TIMEIT")
	print("bsort : ", end = '')
	print(timeit.timeit("bsort([5,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1])", setup = "from __main__ import bsort", number = 10))
	print("qsort : ", end = '')
	print(timeit.timeit("qsort([5,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1])", setup = "from __main__ import qsort", number = 10))