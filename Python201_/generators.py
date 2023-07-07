def number_generator():
    yield 1
    yield 2
    yield 3

# Using the generator function
gen = number_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
