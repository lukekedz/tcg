## TCG

### Description
Initially, interfacing with https://www.tcgplayer.com/ (TCG)'s API for "Magic: The Gathering" card buy/sell data (1/15/21 LK)

### Authors
  0. Luke Kedziora, developer

### Helpful Commands
  0. view files, structure, etc. in Docker IMAGE: `docker run --rm -it --entrypoint=/bin/bash *image name*`

### NOTE:
  0. PostgreSQL database hosted in Google Cloud. In order to interface with DB, need to add *your* IP address to GC Connections (Public IP Authorized Networks)
  1. root requirements.txt is shared in docker-compose, along with `core/`

### Running:
  0. root cli: `pip install -r requirements.txt`
  1. Docker (all):
     - `docker-compose build`, `docker-compose up`
     - multiple? `docker-compose up --scale update_pricing=10`
  2. individual app (typical; exceptions exist):
     - navigate to app directory
     - cli: `python launch.py`

### TODO:
  - `You are using pip version 19.0.3, however version 20.3.3 is available`
  - handle error in TcgApi #request_pricing
  - Docker setup for `update_pricing`
  - instructions on how to run `update_pricing` w/ & w/o Docker (think about setup while developing a new feature/troubleshooting)
  - sku_queue: `This is a development serve. Do not use it in a production deployment.`
  - How can I run `update_pricing` if `sku_queue` is not active? OR ... how can I bypass the call for SKU if env=dev?
  - DB indexing? on which attributes?
  - testing... how can I run a test and/or a report to determine success for updating 65K+ records?
