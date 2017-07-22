with open('two_sum.txt', 'r') as fp:
	nums = [int(line) for line in fp]
	num_set = set(nums)

two_sum = sum(
	any(n - x in num_set and 2 * x != n for x in num_set)
	for n in range(-10000, 10001)
)

print(two_sum)
