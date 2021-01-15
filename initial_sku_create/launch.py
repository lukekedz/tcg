# NOTE: manual import/write of static list of SKUs from Excel
# NOTE: run `python launch.py` from this directory

import sys
sys.path.append('../core')
import db_api
import xlrd

db_api = db_api.DbApi()
conn = db_api.conn()

# NOTE: move to ./core ?
def create(conn, sku):
  cur = conn.cursor()
  cur.execute('INSERT INTO card_prices (sku, created_at, updated_at) VALUES ({}, NOW(), NOW()) ON CONFLICT DO NOTHING'.format(sku))
  conn.commit()

# NOTE: update this file name for init Prod run
file_path = '../excel/dev_SKUs.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

skus = []
for i in range(sheet.nrows):
  skus.append(int(sheet.cell_value(i, 0)))

for sku in skus:
  create(conn, sku)

conn.close()
