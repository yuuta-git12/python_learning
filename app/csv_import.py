# Pythonでのcsvファイルの読み込みのテストコード
# 参考：「シリコンバレー一流プログラマーが教える Pythonプロフェッショナル大全」P237~239

import csv

# csvファイルの作成 書き込み
with open("test.csv", "w", newline="") as csv_file:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    # csvファイルへ書き込む値
    writer.writerow({"Name": "A", "Count": "1"})
    writer.writerow({"Name": "B", "Count": "2"})

# csvファイルの読み込み
# csvファイルから読み込んでdict型に変換し、keyとvalueを表示
# 「,」を含むデータがあるのでreplaceで変換後,float型に変換
sum_value = 0.0
sum_cur_value = 0.0
sum_cur2_value = 0.0
buy_cur1_vol = []
buy_cur2_vol = []
sale_cur1_vol = []
sale_cur2_vol = []
with open(
    "TestTradeHistory_master.csv",
    "r",
) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # for key in row.keys():
        # print(row)
        # print(row.keys)
        # print(row.keys())
        if row["通貨1"] == "SHIB":
            name = "SHIB"
            value1 = float(row["通貨1数量"].replace(",", ""))
            cur_value = float(row["通貨1の対円レート"].replace(",", ""))
            sum_value += value1
            if row["取引種別"] == "買い":  # 購入した金額
                sum_cur_value += cur_value * value1
            else:  # 売った金額
                sum_cur2_value += cur_value * value1
            # 指定した仮想通貨の購入金額と売買金額の平均値の算出
            if row["取引種別"] == "買い":
                buy_cur1_vol.append(float(row["通貨1数量"].replace(",", "")))
                buy_cur2_vol.append(float(row["通貨2数量"].replace(",", "")))
                buy_avg = -sum(buy_cur2_vol) / sum(buy_cur1_vol)
            elif row["取引種別"] == "売り":
                sale_cur1_vol.append(float(row["通貨1数量"].replace(",", "")))
                sale_cur2_vol.append(float(row["通貨2数量"].replace(",", "")))
                sale_avg = -sum(sale_cur2_vol) / sum(sale_cur1_vol)


print("仮想通貨({0})の合計購入枚数：{1}".format(name, sum(buy_cur1_vol)))
print("仮想通貨({0})の合計売買枚数：{1}".format(name, -sum(sale_cur1_vol)))
print("仮想通貨({0})の平均購入価格：{1}円".format(name, buy_avg))
print("仮想通貨({0})の平均売買価格：{1}円".format(name, sale_avg))
