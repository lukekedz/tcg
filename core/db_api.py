from dotenv import load_dotenv
load_dotenv()

import os
import psycopg2
import requests
import sys
from datetime import datetime

# NOTE: connection/methods for AWS PostgreSQL instance
class DbApi:
  def connection(self):
    return psycopg2.connect(
      host = os.getenv(f"{os.getenv('ENV')}_DB_HOST"),
      database = os.getenv(f"{os.getenv('ENV')}_DB_NAME"),
      user = os.getenv(f"{os.getenv('ENV')}_DB_USER"),
      password = os.getenv(f"{os.getenv('ENV')}_DB_PW")
    )

  def assemble_cpkey(self, sku):
    today_str = datetime.now().strftime('%Y%m%d')
    cpkey = today_str + '_' + str(sku)
    return cpkey

  # TODO: is there a better way to write execute statement ...
  # TODO: & potentially eliminate simple syntac errors ?
  def create(self, sku, cpkey, pricing, bl_high):
    try:
      conn = self.connection()
      cur = conn.cursor()

      if pricing:
        cur.execute('''INSERT INTO card_prices (bl_high, direct, low, market, created_at, updated_at, sku, cpkey) VALUES (%(bl_high)s, %(direct)s, %(low)s, %(market)s, %(now)s, %(now)s, %(sku)s, %(cpkey)s);''', {'bl_high': bl_high, 'direct': pricing[2], 'low': pricing[0], 'market': pricing[1], 'now': datetime.now(), 'sku': sku, 'cpkey': cpkey})
        conn.commit()

      conn.close()
    except:
      print('')
      print("#create error:", sys.exc_info()[0])
      print(sku, cpkey, pricing, bl_high)

  # NOTE: not currently in use
  # def find(self, sku):
  #   conn = self.connection()
  #   cur = conn.cursor()
  #   cur.execute('SELECT * FROM card_prices WHERE sku = {}'.format(sku))
    
  #   rows = cur.fetchall()
  #   conn.close()
  #   return rows[0]

  # TODO: no longer needed (along with ./sku_queue) 
  # def request_sku(self):
  #   try:
  #     return requests.request('GET', 'http://sku_queue:5000/tcg_sku').json()
  #   except:
  #     print('')
  #     print("#request_sku error:", sys.exc_info()[0])

  def query_all_sku(self):
    skus = []
    conn = self.connection()
    cur = conn.cursor()

    cur.execute('SELECT sku FROM sku_list')
    rows = cur.fetchall()
    conn.close()

    for sku in rows:
      sku = int(''.join(map(str, sku)))
      skus.append(sku)

    return skus
 