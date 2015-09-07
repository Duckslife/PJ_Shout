TallyBy API
===========
Backend API for TallyBy O2O service which is made by Interpolar, Inc.

Requirements
============
Make sure that you have already the required packages installed before beginning with TallBy API installation

Ubuntu
------

Update your system

```
sudo apt-get update
sudo apt-get upgrade
```

Install the required packages for TallyBy API

```
  sudo apt-get install build-essential python3-dev python-pip libpq-dev
```

Mac
---

Install `postgres` for `psycopg2` dependency
```
brew update
brew install postgres
brew install libffi
```


Installation
============

Install all the project dependencies in requirements.txt

```
  ./install.sh
```

Activate virtualenv

```
  source .venv/bin/activate
```

Start service:

```
  bin/run.sh start
```
