s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as fr:
    print(fr.read())


with open('test.txt', 'r') as fr:
    while True:
        line = fr.readline()
        print(line, end='')
        if not line:
            break

with open('test.txt', 'r') as fr2:
    while True:
        chunk = 2
        line = fr2.read(chunk)
        print(line)
        if not line:
            break

with open('test.txt', 'r') as fr3:
    # print(fr3.tell())
    fr3.seek(5)
    print(fr3.tell())
    print(fr3.read(1))

with open('test.txt', 'w+') as fr4:
    fr4.write(s)
    # write()メソッドの処理によりファイルの位置は最後になっている
    # seekでファイルの位置を最初にする必要がある
    fr4.seek(0) 
    print(fr4.read())

with open('test.txt', 'r+') as fr5:
    print(fr5.read())
    fr5.seek(0)
    fr5.write(s)
    