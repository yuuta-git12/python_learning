import tarfile

# 圧縮してtarファイルを作成する
# open()メソッドを使用するのでwith文を使う
with tarfile.open('/usr/src/app/test_dir/test.tar.gz', 'w:gz') as tr:
    # addメソッドで対象とするディレクトリを指定
    tr.add('testdir')

# tarファイルの展開
with tarfile.open('test.tar.gz', 'r:gz') as tr2:
    tr2.extractall('test_tar')
