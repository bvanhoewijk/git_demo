import sys

def fib(n, cache={}):
	if n in cache:
		return cache[n]
	if n == 0:
		return 0
	if n == 1:
		return 1
	result = fib(n - 1, cache) + fib(n - 2, cache)
	cache[n] = result
	
	return result

# Get some input from sys:
input = int(sys.argv[1])

# Calculate fibonacci
# 38
cache = {}
res = fib(input, cache)

# Print result
print(res)