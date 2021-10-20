from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, other):
        return [str(value) + " " + other for value in self.values]


if __name__ == "__main__":
    # check if this code is working
    print(Counter([1, 2, 3]) + "mississippi")
