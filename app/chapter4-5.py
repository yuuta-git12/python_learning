# -----------------------------------
# 例外処理(エラーハンドリング)
# -----------------------------------

l = [1, 2, 3]
i = 5

try:
    l[0]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('エラーが発生しました')
    print("other:{}".format(ex))
else:
    print("done")
finally:
    print("clean up")


# -----------------------------------
# 独自例外の作成
# -----------------------------------
# Exceptionを継承しているので、大概のエラーはキャッチする
class UppercaseError(Exception):
    print('これは自作エラーです') # 自分で独自の機能を書くことも可能


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word) # 例外は「raise エラーの種類」と書いて発生させることができる


try:
    check()
except UppercaseError as ex:
    print("Error:{}".format(ex))