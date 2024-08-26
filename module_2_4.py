numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for number in numbers:
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
        else:
            not_primes.append(number)
        is_prime = True
print("Primes ", primes)
print("Not Primes: ", not_primes)

# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
# Примечания:
