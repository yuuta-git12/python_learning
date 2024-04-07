import csv
import os
CSV_PATH = "/usr/src/app/roboter/ranking.csv"


def recommend_restaurant():
    count = 0
    val = ''
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r+", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if count < int(row['COUNT']):
                    count = int(row['COUNT'])
                    val = row['NAME']
                else:
                    return val
            return val
    else:
        return 'エラー：CSVファイルが存在しません'


# テストコード
print(recommend_restaurant())