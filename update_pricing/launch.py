# NOTE: local
import atexit
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
# time.sleep(randrange(5, 60))

db_api = db_api.DbApi()
tcg_api = tcg_api.TcgApi()

def update_pricing():
  print('')
  entry = datetime.now()
  print(f"New Interval: {entry.strftime('%H:%M:%S')}")

  sku = db_api.request_sku()
  while sku != 'Anyong!':
    pricing = tcg_api.request_pricing(sku)
    bl_high = tcg_api.public_bl_high(sku)
    db_api.update(sku, pricing, bl_high)
    sku = db_api.request_sku()

  exit_time = datetime.now()
  print(f"Finished!     {exit_time.strftime('%H:%M:%S')}")
  print(f"              {exit_time - entry}")
  print('')

update_pricing()

# NOTE: for repeat runs
# schedule.every(60).minutes.do(update_pricing)
# while 1:
#   schedule.run_pending()
#   time.sleep(1)
