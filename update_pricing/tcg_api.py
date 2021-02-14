from dotenv import load_dotenv
load_dotenv()

import os
import requests

# NOTE: connection/methods for https://www.tcgplayer.com/
class TcgApi:
  HEADERS = { 'Authorization': os.getenv('TCG_AUTH') }
  BL_HIGH_URL = 'http://api.tcgplayer.com/v1.32.0/pricing/buy/sku/'
  PRICING_URL = 'http://api.tcgplayer.com/v1.32.0/pricing/sku/'

  # TODO: much duplication among methods; refactor/consolidate!
  def public_bl_high(self, sku):
    url = TcgApi.BL_HIGH_URL + str(sku)
    response = None
    response = requests.request('GET', url, headers = TcgApi.HEADERS).json()

    if response and response['results'] and response['results'][0]['prices']:
      result = response['results'][0]['prices']
      return result['high']

  def request_pricing(self, sku):
    url = TcgApi.PRICING_URL + str(sku)
    response = None
    response = requests.request('GET', url, headers = TcgApi.HEADERS).json()

    # TODO: handle errors; response just comes back empty
    # NOTE: example
    # { "success": false, "errors": [ "Missing or invalid bearer token." ], "results": [] }
    if response and response['results']:
      result = response['results'][0]
      return [result['lowPrice'] , result['marketPrice'], result['directLowPrice']]
