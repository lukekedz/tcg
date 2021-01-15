import tcg_api

import sys
sys.path.append('../core')
import db_api

db_api = db_api.DbApi()
conn = db_api.conn()
tcg_api = tcg_api.TcgApi()

record = db_api.find(conn, 4517475)
sku = record[0]
pricing = tcg_api.request_pricing(sku)
db_api.update(conn, sku, pricing)
