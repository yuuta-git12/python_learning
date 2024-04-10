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


# CSVファイルの更新処理
# https://algorithm.joho.info/programming/python/csv-update/
def update_list(list, data):
    for i in range(len(list)):
        if list[i]['NAME'] == data['NAME']:
            data['COUNT'] = int(list[i]['COUNT']) + 1
            list[i] = data
    return list


# # テストコード(ranking.csvのレストランのCOUNTアップ処理のテスト)

# ranking.csvのリストへの読み込み
with open(CSV_PATH, "r+", newline="") as csv_file:
    list_test = []
    reader = csv.DictReader(csv_file)
    for row in reader:
        list_test.append(row)

print(list_test)
print(len(list_test))
test_val = "kisa"

flag = restaurant_in_list(list=list_test, name=test_val)

if flag:
    dict = {"NAME": test_val, "COUNT": "0"}
    new_list = update_list(list_test, dict)
    with open(CSV_PATH, "w", newline="") as csv_file:
        fieldnames = ["NAME", "COUNT"]
        writer = csv.DictWriter(csv_file, fieldnames)
        writer.writeheader()
        writer.writerows(new_list)


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
