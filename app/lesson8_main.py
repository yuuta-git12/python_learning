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
from roboter.lib_roboter import restaurant_in_list
from roboter.lib_roboter import update_list
from roboter.lib_roboter import read_csv
from roboter.lib_roboter import write_csv
from roboter.lib_roboter import titlecase

CSV_PATH = "/usr/src/app/roboter/ranking.csv"
HELLO_PATH = "/usr/src/app/roboter/template/template_hello.txt"
LIKE_PATH = "/usr/src/app/roboter/template/template_like_restaurant.txt"
RECOMMEND_PATH = "/usr/src/app/roboter/template/template_recommend.txt"
THANK_PATH = "/usr/src/app/roboter/template/template_thank_you.txt"

# ユーザー名の確認
with open(HELLO_PATH) as f1:
    t1 = string.Template(f1.read())
    print(t1.substitute())
    input_name = input()

# CSVファイルがあるか確認
if os.path.exists(CSV_PATH):
    read_data = read_csv()
    row_count = read_data[1]
    dict_restaurants = read_data[0]
    # csvファイルにデータがない場合
    if row_count < 1:
        with open(LIKE_PATH, "r") as f2:
            t2 = string.Template(f2.read())
            print(t2.substitute(name=input_name))
            # 単語の頭文字が大文字になるようにする
            input_restaurant = titlecase(input())
            write_csv(input_restaurant, 1, False)
    else:
        # COUNTが最大のレストラン名を表示
        dict_recommend_restaurants = recommend_restaurant()
        i = 0
        input_key = "n"
        while i < len(dict_recommend_restaurants) and (
            input_key == "n" or input_key == "No"
        ):
            with open(RECOMMEND_PATH, "r") as f3:
                t3 = string.Template(f3.read())
                print(
                    t3.substitute(
                        recommend_restaurant=dict_recommend_restaurants[i]["NAME"]
                    )
                )
            i = i + 1
            input_key = input()
        # 好きなレストランの質問処理を入れる
        if input_key == "y" or input_key == "Yes":
            with open(LIKE_PATH, "r") as f4:
                t4 = string.Template(f4.read())
                print(t4.substitute(name=input_name))
                input_restaurant = titlecase(input())
                flag = restaurant_in_list(dict=dict_restaurants, name=input_restaurant)
                if flag:
                    dict = {"NAME": input_restaurant, "COUNT": "0"}
                    new_list = update_list(dict_restaurants, dict)
                    with open(CSV_PATH, "w", newline="") as csv_file:
                        fieldnames = ["NAME", "COUNT"]
                        writer = csv.DictWriter(csv_file, fieldnames)
                        writer.writeheader()
                        writer.writerows(new_list)
                else:
                    write_csv(input_restaurant, 1, True)
        else:
            print("エラー：このキーは受け付けられません")
else:
    print("エラー：CSVファイルが存在しません")

# 好きなレストラン名を入力した後、お礼のメッセージを表示する
with open(THANK_PATH, "r") as f5:
    t5 = string.Template(f5.read())
    print(t5.substitute(name=input_name))
