class Foo:
    def __init__(self):
        self.d = {}

    def first(self, printFirst: "Callable[[], None]") -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        self.d[0] = printFirst
        self.check()

    def second(self, printSecond: "Callable[[], None]") -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        self.d[1] = printSecond
        self.check()

    def third(self, printThird: "Callable[[], None]") -> None:

        # printThird() outputs "third". Do not change or remove this line.
        self.d[2] = printThird
        self.check()

    def check(self):
        if len(self.d) == 3:
            self.d[0]()
            self.d[1]()
            self.d[2]()
