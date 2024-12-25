from sys import stdin
from abc import ABC


class Solution(ABC):
    def print_ans(self):
        pass


class NoRoots(Solution):
    def print_ans(self):
        print('No roots')


class OneRoot(Solution):
    def __init__(self, x):
        self.root = x

    def print_ans(self):
        print(f'One root: {self.root}')


class TwoRoots(Solution):
    def __init__(self, x1, x2):
        self.root1 = x1
        self.root2 = x2

    def print_ans(self):
        print(f'Two roots: {self.root1}; {self.root2}')


def solve(a, b, c) -> Solution:
    d = b**2 - 4 * a * c
    if d < 0:
        ans = NoRoots()
    elif d == 0:
        ans = OneRoot(-b / 2 / a)
    else:
        ans = TwoRoots((-b + d**0.5) / 2 / a, (-b - d**0.5) / 2 / a)
    return ans


def main():
    coefs = []
    for i in stdin:
        coefs.append(int(i))
        if len(coefs) >= 3:
            break
    ans = solve(*coefs)
    ans.print_ans()


if __name__ == "__main__":
    main()
