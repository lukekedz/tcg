# NOTE: local
import multiprocessing
import os
# import schedule
import tcg_api
import time
from datetime import datetime

#  NOTE: from core
import sys
sys.path.append('../core')
import db_api

db_api = db_api.DbApi()
skus = db_api.query_all_sku()
tcg_api = tcg_api.TcgApi()

print('')
entry = datetime.now()
print('Launching TCG pricing updates...')
print(f"***ENV*** {os.getenv('ENV').rjust(6)}")
# NOTE: sleep for ENV confirmation
# time.sleep(5)
print(f"Spinning Up: {entry.strftime('%H:%M:%S')}")
print('')

def create_record(sku):
  pricing = tcg_api.request_pricing(sku)
  bl_high = tcg_api.public_bl_high(sku)
  cpkey = db_api.assemble_cpkey(sku)
  print(sku, cpkey, end="\r")
  db_api.create(sku, cpkey, pricing, bl_high)

def process_skus(skus):
  with multiprocessing.Pool() as pool:
    pool.map(create_record, skus)

process_skus(skus)
exit_time = datetime.now()
print('')
print(f"Finished! {exit_time.strftime('%H:%M:%S').rjust(11)}")
print(f"{str(exit_time - entry).rjust(27)}")
print('')

# schedule.every(60).minutes.do(create_record)
# while 1:
  # schedule.run_pending()
  # time.sleep(1)
