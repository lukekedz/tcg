# NOTE: local
import tcg_api

#  NOTE: from core
import sys
sys.path.append('../core')
import db_api

db_api = db_api.DbApi()
tcg_api = tcg_api.TcgApi()

record = db_api.find(4517475)
sku = record[0]
pricing = tcg_api.request_pricing(sku)
print(pricing)
db_api.update(sku, pricing)
