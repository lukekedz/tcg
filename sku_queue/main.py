# NOTE: local
import atexit
from apscheduler.scheduler import Scheduler
from flask import Flask, jsonify
import logging

#  NOTE: from core
import sys
sys.path.append('../core')
import db_api

db_api = db_api.DbApi()
# NOTE: initial run
db_api.query_all_sku()

# NOTE: #query_all_sku for repeat runs
# cron = Scheduler(daemon=True)
# cron.start()
# @cron.interval_schedule(hours = 12)
# def job_function():
    # db_api.query_all_sku()

# NOTE: cron shutdown if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

# NOTE: api
app = Flask(__name__)
@app.route('/')
def home():
  return 'Anyong!'

# NOTE: endpt delivers SKUs until list is empty
@app.route('/tcg_sku')
def tcg_sku():
  if len(db_api.un_updated_skus) >= 1:
    sku = db_api.un_updated_skus.pop()
    return jsonify(sku)
  else:
    # TODO: improve on ?
    return jsonify('Anyong!')

if __name__ == '__main__':
  log = logging.getLogger('werkzeug')
  log.disabled = True

  # NOTE: use if running w/o Docker
  # app.run()
  # NOTE: use with Docker
  app.run(host='0.0.0.0', port=5000, debug=True)
