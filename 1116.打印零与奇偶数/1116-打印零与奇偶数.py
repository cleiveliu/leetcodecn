from queue import Queue
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.to_even = Queue()
        self.to_odd = Queue()
        self.recv = Queue()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n*2+1):
            num = i // 2
            if i & 1 == 1:
                printNumber(0)
            elif num & 1 == 1:
                self.to_odd.put(num)
                self.recv.get()
            else:
                self.to_even.put(num)
                self.recv.get()
                
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n//2):
            num = self.to_even.get()
            printNumber(num)
            self.recv.put(0)
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n+1)//2):
            num = self.to_odd.get()
            printNumber(num)
            self.recv.put(0)