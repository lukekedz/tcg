## TCG

### Description
Initially, interfacing with https://www.tcgplayer.com/ (TCG)'s API for "Magic: The Gathering" card buy/sell data (1/15/21 LK)

### Authors
  0. Luke Kedziora, developer

### Helpful Commands
  0. installing requirements.txt: `pip install -r requirements.txt`

### NOTE:
  0. PostgreSQL database hosted in Google Cloud. In order to interface with DB, need to add *your* IP address to GC Connections (Public IP Authorized Networks)
  1. `./core/` is shared among Docker containers

### TODO:
  0. differentiate/setup ENVs for dev/prod (dev is default; prod explicity set)
