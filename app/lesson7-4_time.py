import datetime
import time

now = datetime.datetime.now()
print(now)
# ISO規格の形式で出力する場合
print(now.isoformat())

# strftimeを使うと、表示形式を自分で設定できる
# 日付・月・西暦(4桁)・時間・分・秒・マイクロ秒
print(now.strftime("%d/%m/%Y-%H%M%S%f"))

# 時間の作成
# １時間10分5秒100マイクロ秒
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H%M%S%f'))


print(now)
# weeks：週、意外に日、時間、分、秒、ミリ秒、マイクロ秒を指定できる
d = datetime.timedelta(weeks=1)
# 1週間後の時刻を表示
print(now + d)
# 1週間前の時刻を表示
print(now - d)


print('#######')
time.sleep(2)
print('#######')

print(time.time())