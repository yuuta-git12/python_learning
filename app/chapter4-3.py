# -----------------------------------
# リスト内包表記の書き方
# -----------------------------------
# タプルからの要素の取り出し（リスト内包表記なし）
t = (1, 2, 3, 4, 5)

r = []
for i in t:
    r.append(i)

print(r)

# タプルからの要素の取り出し（リスト内包表記あり）
t2 = (1, 2, 3, 4, 5)

r2 = [i for i in t2]

print(r2)

# タプルからの偶数の要素だけ取り出す（リスト内包表記なし）
t3 = (1, 2, 3, 4, 5)

r3 = []
for i in t3:
    if i % 2 == 0:
        r3.append(i)

print(r3)
# タプルからの偶数の要素だけ取り出す（リスト内包表記あり）
t4 = (1, 2, 3, 4, 5)

r4 = [i for i in t4 if i % 2 == 0]

print(r4)

# 2つのforループのリスト内包表記
# リスト内包表記無しの場合
t5 = (1, 2, 3, 4, 5)
t6 = (5, 6, 7, 8, 9, 10)

r5 = []
for i in t5:
    for j in t6:
        r5.append(i*j)

print(r5)
# リスト内包表記有りの場合
t7 = (1, 2, 3, 4, 5)
t8 = (5, 6, 7, 8, 9, 10)

r6 = [i * j for i in t7 for j in t8]
print(r6)

# -----------------------------------
# 辞書包括表記の書き方
# -----------------------------------
# 曜日のリストと飲み物のリストを作成し、それらを対応させた辞書を作成
# zip関数を使い、２つのリストの要素を順番に取り出す
# 辞書包括表記を使用しない場合
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 辞書包括表記を使用した場合
w2 = ['mon', 'tue', 'wed']
f2 = ['coffee', 'milk', 'water']

d2 = {x: y for x, y in zip(w, f)}

print(d2)

# -----------------------------------
# 集合内包表記の書き方
# -----------------------------------
# 内包表記で0~9の集合を作成
s = {i for i in range(10)}
print(s)

# 内包表記で0~9の範囲で偶数の集合を作成
s2 = {i for i in range(10) if i % 2 == 0}
print(s2)


# -----------------------------------
# ジェネレーター内包表記の書き方
# -----------------------------------
# forループを使って以下のジェネレーターを作成
def g():
    for i in range(10):
        yield i


g = g()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# 内包表記で書いた場合
g2 = (i for i in range(10))
print(type(g)) # generatorクラスになっているか確認
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

# if文を使用した場合
g3 = (i for i in range(10) if i % 2 == 0)
for x in g3:
    print(x)

# -----------------------------------
# 内包表記でタプルを作成
# -----------------------------------
g4 = tuple(i for i in range(10))
print(type(g4)) # tupleクラスになっているか確認
print(g4)