ranking = {"A": 100, "B": 85, "C": 92}

# 数字の昇順で並び替え
print(sorted(ranking, key=ranking.get))

# 数字の降順で並び替え
print(sorted(ranking, key=ranking.get, reverse=True))


# 文字列sの中に同じ文字が何個あるか調べる処理
s = "fdjsafiewafjdsaeiwfdafke"

d = {}

for c in s:
    # # if文がないと+1加算する対象がなくエラーとなる
    # if c not in d:
    #     d[c] = 0
    d.setdefault(c, 0)
    d[c] += 1

print(d)

# 標準ライブラリdefaultdictを用いた場合
from collections import defaultdict
# 辞書型で初期値が0になる
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)

from termcolor import colored

print(colored('test', 'red'))


import sys

import collections

import lesson_package

print(collections.__file__)
print(lesson_package.__file__)

print(sys.path)