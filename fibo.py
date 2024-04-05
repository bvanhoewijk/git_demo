import sys

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	result = fib(n - 1) + fib(n - 2)
	return result

# Get some input from sys:
input = int(sys.argv[1])

# Calculate fibonacci
# 38
res = fib(input)

# Print result
print(res)