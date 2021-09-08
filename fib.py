
"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The zeroth number in the fibonacci sequence is 0. The first number is 1
Negative numbers should return None
"""
def fibonacci(position):
  if(position == 0): return 0
  if(position == 1 or position == 2):
    return 1
  return fibonacci(position - 1) + fibonacci(position - 2)


# Test cases
print("The 1st Fibonacci number: ", fibonacci(1))
print("The 21st Fibonacci number: ", fibonacci(21))

assert(fibonacci(0) == 0)
print("The 0th Fibonacci number: ", fibonacci(0)) # should return 0

assert(fibonacci(-1) == None)
print("The -1st Fibonacci number: ", fibonacci(-1)) # should return None

print("Code ran successfully!")


