import sys

def fib(n, cache={}):
	"""n= number, cache=dict"""
	if n in cache:
		return cache[n]
	if n == 0:
		return 0
	if n == 1:
		return 1
	result = fib(n - 1, cache) + fib(n - 2, cache)
	cache[n] = result
	
	return result

input = int(sys.argv[1])

cache = {}
res = fib(input, cache)

print(res)