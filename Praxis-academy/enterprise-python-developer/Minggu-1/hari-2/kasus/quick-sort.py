#Quick Sort
def partition(l, r, nums):
	pivot, ptr = nums[r], l
	for i in range(l, r):
		if nums[i] <= pivot:
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr += 1
	nums[ptr], nums[r] = nums[r], nums[ptr]
	return ptr

def quicksort(l, r, nums):
	if len(nums) == 1: 
		return nums
	if l < r:
		pi = partition(l, r, nums)
		quicksort(l, pi-1, nums) 
		quicksort(pi+1, r, nums) 
	return nums

example = [4, 5, 1, 2, 3]
print("Data Awal : \n", example)
print("Data Akhir : \n", quicksort(0, len(example)-1, example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
print("Data Awal : \n", example)
print("Data Akhir : \n", quicksort(0, len(example)-1, example))