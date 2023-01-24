import math
import random


class Bingo(object):
    def __init__(self):
        with open("words.txt", "r") as f:
            self.words = [word[:-1] for word in f.readlines()]

        random.shuffle(self.words)
        self.chosen = set()
        longest_word = max(self.words, key=len)
        self.num_rows = math.ceil(math.sqrt(len(self.words)))
        self.rows = [self.words[i : i + self.num_rows] for i in range(0, len(self.words), self.num_rows)]
        self.cell_size = len(longest_word) + 2
        print("welcome to bingo. try not to shout. enter coordinates space separated (e.g. 0 1)")

    def print_card(self):
        padding = self.cell_size // 4
        print("  ", end="")
        for i in range(self.num_rows):
            print(f"{i: ^{self.cell_size}}", end="")
        print()
        fill = lambda s: "*" if s in self.chosen else " "
        for i, row in enumerate(self.rows):
            fill_row = [fill(entry) * self.cell_size for entry in row]
            for _ in range(padding):
                print(f"  ", end="")
                print(" ".join(fill_row))
            print(f"{i} ", end="")
            print(" ".join([f"{entry:{fill(entry)}^{self.cell_size}}" for entry in row]))
            for _ in range(padding):
                print(f"  ", end="")
                print(" ".join(fill_row))

    def bingo(self):
        was_chosen = lambda s: s in self.chosen
        for row in self.rows:
            if all(was_chosen(s) for s in row):
                return True
        for i in range(self.num_rows):
            col = [self.rows[j][i] for j in range(self.num_rows)]
            if all(was_chosen(s) for s in col):
                return True
        return all(was_chosen(s) for s in [self.rows[i][i] for i in range(self.num_rows)])

    def run(self):
        prompt = "\n"
        while not self.bingo():
            self.print_card()
            user_input = input(prompt + "> ")
            try:
                x, y = tuple(map(int, user_input.split()))
                self.chosen.add(self.rows[y][x])
            except ValueError:
                prompt = "enter two numbers, dInGuS\nLIKE THIS: 0 1\n"
            print("\n" + ("#" * self.cell_size * self.num_rows) + "\n")
        print("BINGO!!!")


if __name__ == "__main__":
    bingo = Bingo()
    bingo.run()
