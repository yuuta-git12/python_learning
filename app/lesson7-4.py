import tempfile

# 一時ファイルの作成　処理が終わったら作成した一時ファイルは消去される
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())


# 一時ファイルを作成し、処理の後も削除しない場合はNamedTemporaryFile関数を使う
# /tmpの中に一時ファイルが作成されている
with tempfile.NamedTemporaryFile(delete=False) as t1:
    # 一時ファイルのパスを表示
    print(t1.name)
    with open(t1.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時ディレクトリの作成　処理が終わったら作成した一時ディレクトリは消去される
with tempfile.TemporaryDirectory() as td:
    print(td)

# 一時ディレクトリの作成　処理が終わっても作成した一時ディレクトリは消去されない
temp_dir = tempfile.mkdtemp()
print(temp_dir)