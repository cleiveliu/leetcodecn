from queue import Queue
class FooBar:
    def __init__(self, n):
        self.n = n
        self.to_foo = Queue()
        self.to_bar = Queue()
        self.to_foo.put(0)
        

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.to_foo.get()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.to_bar.put(0)


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.to_bar.get()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.to_foo.put(0)