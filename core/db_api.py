from dotenv import load_dotenv
load_dotenv()

import os
import psycopg2

# NOTE: connection/methods for Google Cloud PostgreSQL instance
class DbApi:
  def conn(self):
    return psycopg2.connect(
      host = os.getenv('DEV_DB_HOST'),
      database = os.getenv('DEV_DB_NAME'),
      user = os.getenv('DEV_DB_USER'),
      password = os.getenv('DEV_DB_PW')
    )

  def find(self, conn, sku):
    cur = conn.cursor()
    cur.execute('SELECT * FROM card_prices WHERE sku = {}'.format(sku))
    rows = cur.fetchall()
    return rows[0]

  def update(self, conn, sku, pricing):
    cur = conn.cursor()
    if pricing:
      cur.execute('''
        UPDATE card_prices
        SET low = {low}, market = {market}, direct = {direct}, updated_at = NOW()
        WHERE sku = {sku}
      '''.format(sku=sku, low=pricing[0], market=pricing[1], direct=pricing[2]))
      conn.commit()
