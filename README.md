## TCG

### Description
Initially, interfacing with https://www.tcgplayer.com/ (TCG)'s API for "Magic: The Gathering" card buy/sell data (1/15/21 LK)

### Authors
  0. Luke Kedziora, developer

### Helpful Commands
  0. installing requirements.txt: `pip install -r requirements.txt`
  1. view files, structure, etc. in Docker IMAGE: docker run --rm -it --entrypoint=/bin/bash *image name*

### NOTE:
  0. PostgreSQL database hosted in Google Cloud. In order to interface with DB, need to add *your* IP address to GC Connections (Public IP Authorized Networks)
  1. `./core/` is shared among Docker containers; all requirements live here

### Running:
  0. Docker: `docker-compose build`, `docker-compose up`
  1. update_pricing:
     - navigate to directory
     - cli: `python launch.py`

### TODO:
  0. differentiate/setup ENVs for dev/prod (dev is default; prod explicity set)
  1. `You are using pip version 19.0.3, however version 20.3.3 is available`
  2. handle error in TcgApi #request_pricing
  3. Docker setup for `update_pricing`
  4. instructions on how to run `update_pricing` w & w/o Docker (think about setup while developing a new feature/troubleshooting)
