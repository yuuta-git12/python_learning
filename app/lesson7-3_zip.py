import zipfile
import glob

with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('testdir')
    # ディレクトリだけでなく中のファイルも指定する必要がある
    # 指定していないファイルはzipの中には含まれない
    # z.write('testdir/test.txt')
    # ディレクトリの中身を逐一指定するのは面倒なので、globを使って
    # ファイルを一気に指定する
    for f in glob.glob('test_tar/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z1:
    with z1.open('test_tar/testdir/test.csv') as f:
        print(f.read())