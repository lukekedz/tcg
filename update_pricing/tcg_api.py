from dotenv import load_dotenv
load_dotenv()

import os
import requests
import time
from random import randrange

# NOTE: connection/methods for https://www.tcgplayer.com/
class TcgApi:
  HEADERS = { 'Authorization': os.getenv('TCG_AUTH') }
  BL_HIGH_URL = 'http://api.tcgplayer.com/v1.32.0/pricing/buy/sku/'
  PRICING_URL = 'http://api.tcgplayer.com/v1.32.0/pricing/sku/'

  # TODO: much duplication among methods; refactor/consolidate!
  def public_bl_high(self, sku):
    url = TcgApi.BL_HIGH_URL + str(sku)
    response = None

    try:
      response = requests.request('GET', url, headers = TcgApi.HEADERS).json()
    except requests.exceptions.ConnectionError:
      print('#public_bl_high TcgApi timeout')
      time.sleep(randrange(5))
      self.request_pricing(sku)
    except urllib3.exceptions.MaxRetryError:
      print('#public_bl_high TcgApi max retries')
      time.sleep(60)
      self.request_pricing(sku)

    if response and response['results'] and response['results'][0]['prices']:
      result = response['results'][0]['prices']

      bl_high = 'null' if result['high'] is None else result['high']
      return bl_high

  def request_pricing(self, sku):
    url = TcgApi.PRICING_URL + str(sku)
    response = None

    try:
      response = requests.request('GET', url, headers = TcgApi.HEADERS).json()
    except requests.exceptions.ConnectionError:
      print('#request_pricing TcgApi timeout')
      time.sleep(randrange(5))
      self.request_pricing(sku)
    except urllib3.exceptions.MaxRetryError:
      print('#request_pricing TcgApi max retries')
      time.sleep(60)
      self.request_pricing(sku)

    # TODO: handle errors; response just comes back empty
    # NOTE: example
    # { "success": false, "errors": [ "Missing or invalid bearer token." ], "results": [] }
    
    if response and response['results']:
      result = response['results'][0]
      low = 'null' if result['lowPrice'] is None else result['lowPrice'] 
      market = 'null' if result['marketPrice'] is None else result['marketPrice']
      direct = 'null' if result['directLowPrice'] is None else result['directLowPrice']
      return [low, market, direct]
