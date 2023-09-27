import sys

num = 1
name = 'Mike'

# 型の表示
print(num, type(num))
print(name, type(name))

is_OK = True
print(is_OK, type(is_OK))

#　結果は Mike <class 'str'> となる
# numの中身がnameで上書きされ型も値の方に合わせ変化した。
num = name
print(num, type(num))


# 型の変換
name = '1'
new_num = int(name) #数値型に変換
print(new_num, type(new_num))

# 複数の文字列の出力
name = 'Kitty'
print('Hi', 'Mike')
print('Hi', name, 'Mike') #　出力結果：Hi Kitty Mike

print('Hi', name, 'Mike', sep=',', end='\n') # カンマ区切りと改行コードを指定　Hi,Kitty,Mike