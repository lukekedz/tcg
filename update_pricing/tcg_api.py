from dotenv import load_dotenv
load_dotenv()

import os
import requests

# NOTE: connection/methods for https://www.tcgplayer.com/
class TcgApi:
  HEADERS = { 'Authorization': os.getenv('TCG_AUTH') }
  PRICING_URL = 'http://api.tcgplayer.com/v1.32.0/pricing/sku/'

  def request_pricing(self, sku):
    url = TcgApi.PRICING_URL + str(sku)
    response = requests.request('GET', url, headers = TcgApi.HEADERS).json()
    
    # TODO: handle errors; response just comes back empty
    # NOTE: example
    # { "success": false, "errors": [ "Missing or invalid bearer token." ], "results": [] }
    
    if response['results']:
      result = response['results'][0]
      low = 'null' if result['lowPrice'] is None else result['lowPrice'] 
      market = 'null' if result['marketPrice'] is None else result['marketPrice']
      direct = 'null' if result['directLowPrice'] is None else result['directLowPrice']
      return [low, market, direct]
