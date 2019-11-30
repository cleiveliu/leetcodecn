class Solution:
    def mySqrt(self, x: int) -> int:
        def is_it(guess, target) -> bool:
            if guess * guess <= target and (guess + 1) * (guess + 1) > target:
                return True
            else:
                return False

        def new_guess(oldguess, target):
            return (oldguess + target // oldguess) // 2

        if x < 1:
            return 0
        guess = 1
        while not is_it(guess, x):
            guess = new_guess(guess, x)

        return guess
