# 4-2.関数の応用をマスターしよう
# 関数内関数の書き方
# 関数内関数(Inner function)関数の中に定義された関数
# 関数の中だけで繰り返し使う処理があるような場合に作成するとよい
def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)


# 関数内関数とクロージャー
# 関数内関数をクロージャーと呼ぶことがある
def outer2(a, b):
    def inner():
        return a + b

    return inner


# a + bの結果ではなくinnerのオブジェクトを返す
print(outer2(1, 2))
# 関数outerの返り値を格納し、格納したものを実行
# この場合、innerの中のa、bには関数outer呼び出し時の引数である、1と2が格納されており
# f()で3が返ってくる。このようなとき、関数内関数のことをクロージャーという。
# クロージャーを使うと、外側の関数に渡す引数で、関数内関数の状態を変えることができる
f = outer2(1, 2)
r = f()
print(r)


# 関数内関数とクロージャー２
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)
print(ca1(10))
print(ca2(10))


# クロージャー3
def counter_func():
    def returnCounter(count):
        return count + 1

    return returnCounter


myCounter1 = counter_func()
myCounter2 = counter_func()
print(myCounter1(2))
print(myCounter2(3))


# デコレーターで関数の前後に処理を加える
def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


def print_more(func):
    def wrapper(*args, **kwargs):
        print("func:", func.__name__)
        print("args:", args)
        print("kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result

    return wrapper


@print_info
@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)

# @を使わない複数デコレーターの書き方
f = print_info(print_more(add_num))
r = f(10, 20)
print(r)

# -------------------------------------
# lambda（無名関数）を使って関数を引数にする
# -------------------------------------
# lambdaは、短い関数を簡潔に定義して、いろいろな用途で使えるようにするテクニック

# lambdaを使わない例
l = ["Mon", "tue", "Wed", "Thu", "Fri", "sat", "Sun"]


# 引数wordsのリストを、funcで指定された関数で処理し、その結果をコンソールに表示する
def change_words(words, func):
    for word in words:
        print(func(word))


# 文字列を大文字に変更する関数
def sample_func(word):
    return word.capitalize()


change_words(l, sample_func)

# lambdaを使った例
# lambdaの後のwordが引数として渡され、word.capitalize()が返り値として
# 返ってくる関数という子を示している。lambdaを使うとreturnを書かなくて良いので行数が少なくてすむ
# lambda 引数: 結果を返す処理
sample_func_lambda = lambda word: word.capitalize()
change_words(l, sample_func_lambda)

# 別の書き方
change_words(l, lambda word: word.capitalize())

# lambdaは単純な関数を複数定義するときに使うと、よりその有効性を感じることができる
# 例えば文字列を小文字にするための処理をlowerメソッドを使い作成したいとする。


# lambdaなしの場合 小文字に変換するための関数を追加する必要がある
def sample_func2(word):
    return word.lower()


change_words(l, sample_func2)

# lambdaを使った場合
change_words(l, lambda word: word.lower())

# -----------------------------------
# ジェネレーターで反復可能な要素を生成する
# -----------------------------------
# イテレーター（反復可能オブジェクトのこと）：リストや辞書などの総称
# イテレーターに対して反復処理を行う際には、あらかじめ用意された要素を
# forループなどで取り出していた。
# これに対して、ジェネレーターは、イテレーターと同じ反復処理だが、
# 要素を取り出すときにそのつど要素を生成している。

# イテレーターの処理
l = ["Good morning", "Good afternoon", "Good night"]

for i in l:
    print(i)


# 同様の処理をジェネレーターで書いた場合
# ジェネレーターではreturnではなく、yieldを使う
def greeting():
    yield "Good morning"
    yield "Good afternoon"
    yield "Good night"


for g in greeting():
    print(g)

# next関数（イテレーターの次の要素を取得する関数）を使って１つずつ出力した例
g = greeting()
# print(next(g))
# print('@@@@@@@@@')
# print(next(g))
# print('@@@@@@@@@')
# print(next(g))

# 複数のジェネレーターを取り混ぜて使った場合
def counter(num=10):
    for i in range(num):
        yield "run" + str(i)


c = counter()

print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
