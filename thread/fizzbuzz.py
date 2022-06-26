import threading

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.f = threading.Lock()
        self.b = threading.Lock()
        self.fb = threading.Lock()
        self.main = threading.Lock()
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        for i in range (self.n // 3 - self.n // 15):
            self.f.acquire()
            printFizz()
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        for i in range (self.n // 5 - self.n // 15):
            self.b.acquire()
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        for i in range (self.n // 15):
            self.fb.acquire()
            printFizzBuzz()
            self.main.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        for i in range(1, self.n + 1):
            self.main.acquire()
            if i % 15 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release()

solution = FizzBuzz(15)
solution.number()
