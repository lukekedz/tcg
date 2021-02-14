# NOTE: one-time manual import/write of static list of SKUs from Excel
# NOTE: run `python launch.py` from this directory

import sys
sys.path.append('../core')
import db_api
import multiprocessing
import xlrd

# NOTE: c/o for environment choice
# file_path = '../excel/dev_SKUs.xls'
# file_path = '../excel/prod_SKUs.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

skus = []
for i in range(sheet.nrows):
  skus.append(int(sheet.cell_value(i, 0)))

# TODO: refactor; not best practice
DB_API = db_api.DbApi()

def create(sku):
  conn = DB_API.connection()
  cur = conn.cursor()
  cur.execute('INSERT INTO sku_list (created_at, updated_at, sku) VALUES (NOW(), NOW(), {}) ON CONFLICT DO NOTHING'.format(sku))
  conn.commit()
  conn.close()

def process_skus(skus):
  with multiprocessing.Pool() as pool:
    pool.map(create, skus)

process_skus(skus)
