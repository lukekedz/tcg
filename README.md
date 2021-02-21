## TCG

### Description
Initially, interfacing with https://www.tcgplayer.com/ (TCG)'s API for "Magic: The Gathering" card buy/sell data (1/15/21 LK)

### Authors
  0. Luke Kedziora, developer

### Helpful Commands
  0. d/l pip: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  1. install pip: python get-pip.py
  2. install requests (HTTP): python -m pip install requests
  3. install dotenv: python -m pip install python-dotenv
  4. install psycopg2: python -m pip install psycopg2-binary
  5. view files, structure, etc. in Docker IMAGE: `docker run --rm -it --entrypoint=/bin/bash *image name*`

### NOTE:
  0. PostgreSQL database hosted in AWS. In order to interface with DB, need to add *your* IP address to "edit inbound rules" (https://serverfault.com/questions/656079/unable-to-connect-to-public-postgresql-rds-instance/656119#656119)
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
  - Docker setup for `update_pricing` ?
  - instructions on how to run `update_pricing` w/ & w/o Docker (think about setup while developing a new feature/troubleshooting)
  - testing... how can I run a test and/or a report to determine success for updating 65K+ records?
  - now, not using docker-compose. clean up repo to reflect (& update Running cmds)
  - do I need update_pricing/requirements.txt now?

### HOTLIST:
  0. automate so running daily w/o manual launch (on cron job)
  0a. automate so laptop doesn't have to be runnning
  0b. automated process to update TCG bearer token
  1. verify pricing has usable data... meaning it looks current logic will return None from TcgAPi if there is a problem, and there is nothing to catch/verify/notify on that lack of data
  2. save oft-used SQL commands in DBeaver (wipe out testing work) (& where does DBeaver store these?)
  3. error handling/reporting from TcgApi/DbApi (removed quite a bit due to success of multiprocessing upon AWS launch 2/14)
  4. when is AWS daily maintenance scheduled for? does this affect normal operations?
