#DOMASHKA
#1

class PrimeGenerator:
    def __init__(self):
        self.primes = []
        self.num = 2

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate(self):
        while True:
            if self.is_prime(self.num):
                self.primes.append(self.num)
                yield self.num
            self.num += 1

prime_gen = PrimeGenerator()
prime = prime_gen.generate()

print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime)) 