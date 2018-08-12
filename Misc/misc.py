
def genPrimes():
    list_of_primes = []
    i = 1
    while True:
        i += 1
        for prime in list_of_primes:
            if i%prime == 0:
                break
        else:
            list_of_primes.append(i)
            yield i

print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())
print(genPrimes().__next__())