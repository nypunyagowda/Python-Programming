def check_prime(num):
    if num < 2:
        print(f"{num} is not prime.")
        return

    # Look for factors
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime (found factor: {i})")
            break  # This skips the 'else' block
    else:
        # This only runs if the loop finished without hitting 'break'
        print(f"{num} is a prime number!")

# Testing the logic
check_prime(7)
check_prime(10)