import csv
import os

CSV_PATH = "/usr/src/app/roboter/ranking.csv"


# CSV内のデータを項目名以外全てCOUNTで降順にして返す
def recommend_restaurant():
    list = []
    # print(type(dict))
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r+", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                dict = {"NAME": row["NAME"], "COUNT": row["COUNT"]}
                list.append(dict)
            # COUNTをキーにして降順に変更
            return sorted(list, key=lambda x: x["COUNT"], reverse=True)
    else:
        return "エラー：CSVファイルが存在しません"


# レストラン名だけのリストに入力したレストラン名が存在するか否かを返すメソッド
def restaurant_in_list(list=[], name=""):
    list_restaurant = []
    for val in list:
        list_restaurant.append(val["NAME"])
    return name in list_restaurant




# # テストコード
list_test = recommend_restaurant()

test_val = "Japanese Test"

print(restaurant_in_list(list=list_test, name="0o"))


# # リストの中に入力値が含まれるか確認
# print(test_val in list_val)

# # print(type(recommend_restaurant()))
# # # 辞書型のキーだけ表示
# for key in list:
#     print(key.get('NAME'))
# # 辞書型の値だけ表示
# for value in list:
#     print(value.get('COUNT'))
# input_val = 'n'
# i = 0
# while i < len(list) and input_val == 'n':
#     print(list[i]['NAME'])
#     i = i + 1
#     input_val = input()
