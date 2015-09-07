GroupBy API
===========
Backend API for Groupby service which is made by privately.

Requirements
============
Make sure that you have already the required packages installed before beginning with GroupBy API installation

Ubuntu
------

Update your system

```
sudo apt-get update
sudo apt-get upgrade
```

Install the required packages for GroupBy Api

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
