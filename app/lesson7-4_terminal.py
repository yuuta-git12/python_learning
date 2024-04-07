import subprocess

# subprocessを使うとターミナル用のコマンドをpythonで実行できる
subprocess.run(['ls'])
# コマンドのオプションを追加するには、引数のリストに追加する
subprocess.run(['ls', '-al'])
# run関数の引数、shellをTrueにすると、リストを使わずに
# オプション付きのコマンドを実行できる
subprocess.run('ls -al', shell=True)
# shell=Trueを使う場合、|(パイプ)も使用できる
subprocess.run('ls -al | grep test', shell=True)

# shell=Trueを使い、存在しないコマンドを実行した場合は0以外の値が返ってくる
# コマンドの処理がエラーになっても以降のプログラムは実行される
# check=Trueを入れると、コマンドでエラーになった場合、PythonでExceptionが
# 発生し処理が止まる
r = subprocess.run('lal | grep test', shell=True, check=True)
print('test')
print(r.returncode)

# コマンドをリストに格納する方法では、実行コマンドでエラーが起きた場合は
# PythonでExceptionが発生し、処理が止まる
# コマンドをリストに格納する方法で、パイプを使いたい場合はPopenを使う