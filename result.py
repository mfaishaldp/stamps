def is_prime(n): # Function to check if a number is prime
    if n < 2: # numbers < 2 are not prime
        return False
    for i in range(2, int(n**0.5) + 1): # check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 101)) # Create a list of numbers from 1 to 100
numbers.reverse() # Reverse the list so we start from 100 down to 1

result = [] # this will hold our final output
for n in numbers:
    if is_prime(n):
        continue # skip prime numbers (do not include them in output)
    if n % 15 == 0: # divisible by both 3 and 5
        result.append("FooBar")
    elif n % 3 == 0: # divisible by 3 only
        result.append("Foo")
    elif n % 5 == 0: # divisible by 5 only
        result.append("Bar")
    else:
        result.append(str(n)) # keep the number itself as a string

print(" ".join(result)) # Print all results horizontally, separated by spaces