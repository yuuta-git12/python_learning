def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)


# 関数を呼び出すときは()を付けること
# ()を付けずに実行すると、エラーは出ないが、関数内の処理が実行されない
# 例：something
say_something("Hi!", "Mike", "Nancy")

# typeで型を確認する場合は()は不要　この場合、functionという型であることが分かる
print(type(say_something))

# 関数もfunction型の値(オブジェクト)なので、変数に入れてからの実行も可能
# f = say_something
# f()


# 関数を呼び出した後、返り値が必要な場合はreturnを使用
def say_something2():
    s = "hi"
    return s


result = say_something2()
print(result)


# 引数
# 引数と返り値の型変換はできるが、異なる型を渡してもエラーは返さない
def what_is_this(color: str) -> str:
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green papper"
    else:
        return "I don't know"


# result = what_is_this(3)
# print(result)


def sample_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = sample_func(100)
print(r)

r = sample_func(100)
print(r)


# 位置引数のタプル化
# 関数に渡す引数を増やす方法
# 1.関数の定義を変更
# 2.引数を*argsのように*付きにすると、複数の引数をタプルでまとめてくれる
def say_something3(*word):
    print(word)
    for arg in word:
        print(arg)


say_something3("Hi!", "Mike", "Nancy")


# タプルと位置引数を混ぜて使うこともできる
# 最初の引数が必須で残りの引数がの数が不明の場合に役立つ
def say_something4(word, *args):
    print("word", word)
    for arg in args:
        print(arg)


say_something4("Hi!", "Mike", "Nancy")


# キーワード引数を辞書化してまとめる
# 関数に渡すキーワード引数の数を変更する場合は、キーワード引数の辞書化という方法がある
def menu(entree="beef", drink="wine"):
    print(entree, drink)


menu(entree="beef", drink="coffee")


# 関数の引数に**kwargsのように**を付けることで、キーワード引数を辞書型で受け取ることができる。
def menu2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu2(entree="beef", drink="coffee")


# キーワード引数を辞書にして渡す
# 関数に渡す変数の前に**を付ける
def menu3(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


d = {
    "entree": "beef",
    "drink": "ice coffee",
    "dessert": "ice",
}
menu3(**d)


# 位置引数とタプル化と辞書化の組み合わせ
def menu4(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu4("banana", "apple", "orange", entree="beef", drink="coffee")

# docstring
# Pythonの関数の説明を記述するための文章
# 関数の説明や、引数及び返り血の説明や型について記述する
def example_func(param1, param2):
    """Docstring example for describing overall explanation of function
    
    Args:
        param1(int): The firts parameter.
        param2(str): The second parameter.
    
    Returns:
        bool: The return value. True for success, False otherwise.
    
    """
    print(param1)
    print(param2)
    return True

# docstringの内容が確認できる
print(example_func.__doc__)
# help関数でもdocstringの内容が確認できる
help(example_func)