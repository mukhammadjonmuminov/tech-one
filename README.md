1. Docker compose install
```bash
pip install docker-compose
```

2. Docker compose run
```bash
docker-compose up
```
```
CREATE DATABASE eduon;

CREATE USER mustafo WITH PASSWORD 'mustafo4530';

ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE eduon TO mustafo;
```

```
export POSTGRES_DB=eduon
export POSTGRES_USER=mustafo
export POSTGRES_PASSWORD=mustafo4530
```

```bash

# sudo nano /etc/systemd/system/gunicorn.service
Environment="POSTGRES_DB=edustudy"
Environment="POSTGRES_USER=mustafo"
Environment="POSTGRES_PASSWORD=mustafo4530"
```

```
Server user - mustafo
password - mustafo
```
#   o n e - t e c h  
 #   t e c h  
 