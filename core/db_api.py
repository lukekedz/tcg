from dotenv import load_dotenv
load_dotenv()

import os
import psycopg2
import requests
import sys

# NOTE: connection/methods for Google Cloud PostgreSQL instance
class DbApi:
  def __init__(self):
    self.un_updated_skus = []

  def connection(self):
    return psycopg2.connect(
      host = os.getenv(f"{os.getenv('ENV')}_DB_HOST"),
      database = os.getenv(f"{os.getenv('ENV')}_DB_NAME"),
      user = os.getenv(f"{os.getenv('ENV')}_DB_USER"),
      password = os.getenv(f"{os.getenv('ENV')}_DB_PW")
    )

  def find(self, sku):
    conn = self.connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM card_prices WHERE sku = {}'.format(sku))
    
    rows = cur.fetchall()
    conn.close()
    return rows[0]

  def request_sku(self):
    try:
      return requests.request('GET', 'http://sku_queue:5000/tcg_sku').json()
    except:
      print('')
      print("#request_sku error:", sys.exc_info()[0])

  def query_all_sku(self):
    self.un_updated_skus = []
    conn = self.connection()

    cur = conn.cursor()
    cur.execute('SELECT sku FROM card_prices')
    rows = cur.fetchall()
    conn.close()

    for sku in rows:
      sku = int(''.join(map(str, sku)))
      self.un_updated_skus.append(sku)

  def update(self, sku, pricing):
    try:
      conn = self.connection()
      cur = conn.cursor()
    except:
      print('')
      print("#update connection error:", sys.exc_info()[0])

    try:
      if pricing:
        cur.execute('''
          UPDATE card_prices
          SET low = {low}, market = {market}, direct = {direct}, updated_at = NOW()
          WHERE sku = {sku}
        '''.format(sku=sku, low=pricing[0], market=pricing[1], direct=pricing[2]))
        conn.commit()
      conn.close()
    except:
      print('')
      print("#update execute error:", sys.exc_info()[0])
 