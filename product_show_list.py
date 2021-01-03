import pandas as pd
from datetime import date

product_backup_path = 'data/20201230_product_backup.csv'
aiaomei_data_path = 'data/aiaomei_product_data.csv'

product_data = pd.read_csv(product_backup_path, header=0, error_bad_lines=False)
product_data_merge = product_data.drop(columns=['商品数量(件)'])
product_data_merge['商品'] = product_data_merge['商品'].str.strip()
print(product_data_merge)

aiaomei_data = pd.read_csv(aiaomei_data_path, header=0, error_bad_lines=False)
print(aiaomei_data.columns)
aiaomei_data_merge = aiaomei_data[
    ['sku_id', 'sales_price_RMB', 'agency_price_RMB', 'agency_price_AUD', 'agency_profit_RMB']].rename(
    columns={'sku_id': 'SKU'}).drop_duplicates('SKU', keep='last')
print(aiaomei_data_merge)

product_show_list = product_data_merge.merge(aiaomei_data_merge, on='SKU').rename(
    columns={
        'sales_price_RMB': '售价(RMB)',
        'agency_price_RMB': '进价(RMB)',
        'agency_price_AUD': '进价(AUD)',
        'agency_profit_RMB': '利润(RMB)'
    }).round(2)

product_show_list['利润率(%)'] = round(product_show_list['利润(RMB)']/product_show_list['进价(RMB)']*100, 2)
product_show_list['成本折扣(折)'] = round(product_show_list['进价(RMB)']/product_show_list['售价(RMB)']*10, 2)
product_show_list = product_show_list.sort_values(['成本折扣(折)'], ascending=1)

product_show_list.to_csv(f'data/product_show_list_{date.today()}.csv', index=False)
print(product_show_list)
