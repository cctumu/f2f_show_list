import unittest
import pandas as pd

product_show_list_data = pd.read_csv(
    'data/product_show_list_2021-01-01.csv', header=0, error_bad_lines=False
)
product_backup_list_data = pd.read_csv(
    'data/20201230_product_backup.csv', header=0, error_bad_lines=False
).dropna(how='all')


class ProductShowListTestCase(unittest.TestCase):
    def test_columns(self):
        self.assertListEqual(list(product_show_list_data.columns),
                             ['SKU', '商品', '商品规格', '售价(RMB)', '进价(RMB)', '进价(AUD)', '利润(RMB)', '利润率(%)', '成本折扣(折)'])

    def test_rows(self):
        self.assertEqual(len(product_backup_list_data.index), len(product_show_list_data.index))


if __name__ == '__main__':
    unittest.main()
