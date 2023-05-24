def fibonacci(n, k):
    """Generate Fibonacci sequence up to n terms."""
    fib_seq = [0, 1]  # Starting sequence
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])  # Add the sum of the last two number
    if k in fib_seq:
        return True
    else:
        return False


n = 20  # Number of Fibonacci numbers to generate
fib_numbers = fibonacci(n, 7)
print(fib_numbers)
