import csv
import os

CSV_PATH = "/usr/src/app/roboter/ranking.csv"


# CSV内のデータをCOUNTで降順にして返す
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
def restaurant_in_list(dict=[], name=""):
    list_restaurant = []
    for val in dict:
        list_restaurant.append(val["NAME"])
    return name in list_restaurant


# CSVファイルの更新処理
# https://algorithm.joho.info/programming/python/csv-update/
def update_list(list, data):
    for i in range(len(list)):
        if list[i]["NAME"] == data["NAME"]:
            data["COUNT"] = int(list[i]["COUNT"]) + 1
            list[i] = data
    return list


# CSVファイルにデータを書き込む処理
# def write_csv():


# # テストコード(ranking.csvのレストランのCOUNTアップ処理のテスト)

# ranking.csvのリストへの読み込み
with open(CSV_PATH, "r+", newline="") as csv_file:
    list_test = []
    reader = csv.DictReader(csv_file)
    for row in reader:
        list_test.append(row)


# csvの行数、csvの中身を辞書型で返す
# 複数の戻り値が使えるか確認
def read_csv():
    with open(CSV_PATH, "r", newline="") as csv_file:
        dict_restaurants = []
        reader = csv.DictReader(csv_file)
        row_count = 0
        for row in reader:
            dict_restaurants.append(row)
            row_count += 1
    return dict_restaurants, row_count


# CSVへの書き込み関数
# update_flagがTrueで追記、Falseで上書き
def write_csv(input_restaurant, count, update_flag=False):
    if not update_flag:
        with open(CSV_PATH, "w", newline="") as csv_file:
            fieldnames = ["NAME", "COUNT"]
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()
            writer.writerow({"NAME": input_restaurant, "COUNT": count})
    else:
        with open(CSV_PATH, "a", newline="") as csv_file:
            fieldnames = ["NAME", "COUNT"]
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writerow({"NAME": input_restaurant, "COUNT": count})

