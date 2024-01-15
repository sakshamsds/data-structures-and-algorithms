class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_bulls, num_cows = 0, 0

        secret_counter = collections.Counter(secret)
        guess_counter = collections.Counter(guess)
        # print(secret_counter)

        for d1, d2 in zip(secret, guess):
            if d1 == d2:
                num_bulls += 1
                secret_counter[d1] -= 1
                guess_counter[d2] -= 1
        # print(secret_counter)

        # g - 0 -> 10, s - 0 -> 4   cows = 5
        # g - 0 -> 6, s - 0 -> 10   cows = 4
        for digit, freq in guess_counter.items():
            if digit in secret_counter:
                num_cows += min(guess_counter[digit], secret_counter[digit])

        return f'{num_bulls}A{num_cows}B'
        