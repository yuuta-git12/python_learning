import collections
import csv
import os
import pathlib


RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'


class CsvModel(object):
    def __init__(self, csv_file) -> None:
        self.csv_file = csv_file
        # csvファイルが存在しない場合はtouchメソッドでファイルを作成
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()


class RankingModel(CsvModel):
    def __init__(self, csv_file=None, *args, **kwargs) -> None:
        if not csv_file:
            csv_file = self.get_csv_file_path()

        super().__init__(csv_file, *args, **kwargs)
        self.column = [RANKING_COLUMN_NAME, RANKING_COLUMN_COUNT]
        self.data = collections.defaultdict(int)
        self.load_data()

    def get_csv_file_path(self):
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        return csv_file_path
    
    def load_data(self):
        with open(self.csv_file, 'w+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row[RANKING_COLUMN_NAME]] = int(
                    row[RANKING_COLUMN_COUNT]
                )
        return self.data
    
    def save(self):
        with open(self.csv_file, 'w+', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_NAME: name,
                    RANKING_COLUMN_COUNT: count
                })

    def get_most_popular(self, not_list=None):
        if not_list is None:
            not_list = []

        if not self.data:
            return None
        
        # self.data.getはself.dataのkey?value?
        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        # sorted_dataがcsvに存在しているデータ
        # not_list:紹介済みのレストランのデータを入れるリスト
        for name in sorted_data:
            if name in not_list:
                continue
            return name
    
    
