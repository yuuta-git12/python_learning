# -----------------------------------
# 変数の有効範囲
# -----------------------------------
animal = "cat"


def f():
    # global animal
    animal = "dog"
    pet = "neko"
    print("local:", locals())


f()
print("global:", animal)
