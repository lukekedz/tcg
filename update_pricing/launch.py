# NOTE: local
import atexit
import schedule
import tcg_api
import time
from datetime import datetime

#  NOTE: from core
import sys
sys.path.append('../core')
import db_api

# NOTE: give time for other services to spin-up
time.sleep(10)

db_api = db_api.DbApi()
tcg_api = tcg_api.TcgApi()

def update_pricing():
  print('')
  entry = datetime.now().strftime("%H:%M:%S")
  print(f"New Interval: {entry}")

  sku = db_api.request_sku()
  while sku != 'Anyong!':
    pricing = tcg_api.request_pricing(sku)
    db_api.update(sku, pricing)
    # NOTE: and repeat
    sku = db_api.request_sku()

  exit_time = datetime.now().strftime("%H:%M:%S")
  print(f"Fin: {exit_time}")
  print('')

update_pricing()

schedule.every(10).minutes.do(update_pricing)
while 1:
    schedule.run_pending()
    time.sleep(1)
