def duplicate_number(nums):
	total = 0
	current = 0
	for num in nums:
		current += num
	for i in range(0,len(nums)-1):
		total+= i
	print(current-total)


duplicate_number([0, 2, 3, 1, 4, 5, 3])