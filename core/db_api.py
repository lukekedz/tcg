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
