import math
class Count(object):
    def __init__(self, start=0, step=1, stop=10):
        self.n = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        self.firstNumber = 0
        self.secondNumber = 1
        self.primes =  0
        self.wynik = 0
        return self

    def __next__(self):
        n = self.n
        self.n += self.step
        primes = self.primes
        wynik = self.wynik
        if self.n == 2:
            self.primes = self.n
        else:
            for i in range(2, self.n):
                if (self.n % i) != 0:
                    self.primes = self.n
                else:
                    break

        fibonacci = self.firstNumber
        if fibonacci > self.stop:
            raise StopIteration
        self.firstNumber, self.secondNumber = self.secondNumber, self.firstNumber + self.secondNumber
        wynik=math.sqrt(fibonacci**2+primes**2)

        return n, fibonacci, primes, wynik


for x in Count(0, 1, 1000):
    print(x)
