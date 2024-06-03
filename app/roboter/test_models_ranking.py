import unittest
from models import ranking
import string


class RankingTest(unittest.TestCase):
    # 指定したcsvファイルが存在しない時、そのcsvファイルが作成されることを
    # 確認するテスト
    def test_csv(self):
        test_ranking = ranking.CsvModel('ranking.csv')
        self.assertEqual('testresult', test_ranking)
    

if __name__ == "__main__":
    unittest.main()