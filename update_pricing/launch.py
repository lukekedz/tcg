# NOTE: local
import atexit
import multiprocessing
import schedule
import tcg_api
import time
from datetime import datetime
from random import randrange

#  NOTE: from core
import sys
sys.path.append('../core')
import db_api

# NOTE: give time for other services to spin-up
# NOTE: and stagger containers
# time.sleep(randrange(5, 20))

db_api = db_api.DbApi()
db_api.query_all_sku()
tcg_api = tcg_api.TcgApi()

def process_skus(skus):
  with multiprocessing.Pool() as pool:
    pool.map(update_pricing, skus)

# def update_pricing():
def update_pricing(sku):
  # print('')
  # entry = datetime.now()
  # print(f"New Interval: {entry.strftime('%H:%M:%S')}")

  # sku = db_api.request_sku()
  # while sku != 'Anyong!':

  pricing = tcg_api.request_pricing(sku)
  # TODO: verify pricing has usable data
  bl_high = tcg_api.public_bl_high(sku)
  db_api.update(sku, pricing, bl_high)
  # sku = db_api.request_sku()

  # exit_time = datetime.now()
  # print(f"Finished!     {exit_time.strftime('%H:%M:%S')}")
  # print(f"              {exit_time - entry}")
  # print('')

# update_pricing()
process_skus(db_api.un_updated_skus)

# NOTE: for repeat runs
# schedule.every(60).minutes.do(update_pricing)
# while 1:
  # schedule.run_pending()
  # time.sleep(1)
