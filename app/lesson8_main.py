# roboter
# ユーザーに好きなレストランを質問しその結果をファイルに記録する
# CSVファイルに記録されたレストランの情報をもとに、
# ユーザーにレストランをお勧めする
# 同じレストランが解凍された場合は　レストランの数字COUNT(票を+1する)
# レストランのお勧め後に、そのレストランが好きかどうかユーザーに尋ねる
# 回答がNoだった場合は他のレストランのデータあればそれをお勧めする

# アプリケーション起動時はユーザーに名前を尋ねるようにする
# 後のメッセージ表示で使用する

import string
import csv
import os
from roboter.lib_roboter import recommend_restaurant

CSV_PATH = "/usr/src/app/roboter/ranking.csv"
HELLO_PATH = "/usr/src/app/roboter/template/template_hello.txt"
LIKE_PATH = "/usr/src/app/roboter/template/template_like_restaurant.txt"
RECOMMEND_PATH = "/usr/src/app/roboter/template/template_recommend.txt"

# ユーザー名の確認
with open(HELLO_PATH) as f1:
    t1 = string.Template(f1.read())
    print(t1.substitute())
    input_name = input()

# 好きなレストランの確認
# csvファイルの存在の確認
# csvファイルに2行以上書き込みがあるか

if os.path.exists(CSV_PATH):
    with open(CSV_PATH, "r+", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        row_count = sum(1 for row in reader)
        if row_count < 2:
            with open(LIKE_PATH, 'r') as f2:
                t2 = string.Template(f2.read())
                print(t2.substitute(name=input_name))
                input_restaurant = input()
                fieldnames = ["NAME", "COUNT"]
                writer = csv.DictWriter(csv_file, fieldnames)
                writer.writeheader()
                writer.writerow({"NAME": input_restaurant, "COUNT": "1"})
        else:
            # COUNTが最大のレストラン名を表示
            read_recommend_restaurant = recommend_restaurant()
            with open(RECOMMEND_PATH, 'r') as f3:
                t3 = string.Template(f3.read())
                print(t3.substitute(recommend_restaurant=read_recommend_restaurant))
            
            # yes/noの場合の処理を記述する
            # yes 処理終了のメッセージ
            # no 他のおすすめのレストランを表示する
            # 好きなレストランの質問処理を入れる





# with open("/usr/src/app/roboter/template_thank_you.txt") as f3:
#     t3 = string.Template(f3.read())
#     print(t3.substitute(name=input_name))
