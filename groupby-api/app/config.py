# -*- coding: utf-8 -*-

import os
import configparser

APP_ENV = os.environ.get('APP_ENV') or 'dev'  # or 'live' to load live
INI_FILE = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../conf/{}.ini'.format(APP_ENV))

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

ONE_HOUR = 21600
TOKEN_LEN = 24
TOKEN_EXPIRES = ONE_HOUR
SECRET_KEY = 'YkX0dBv77CItuIBMyljLVPBUSuYTGpvGaXFi31LXPm0='

if APP_ENV == 'dev' or APP_ENV == 'live':
    DB_CONFIG = (CONFIG['postgres']['user'], CONFIG['postgres']['password'], CONFIG['postgres']['host'], CONFIG['postgres']['database'])
    DATABASE_URL = "postgresql+psycopg2://%s:%s@%s/%s" % DB_CONFIG
else:
    DB_CONFIG = (CONFIG['postgres']['host'], CONFIG['postgres']['database'])
    DATABASE_URL = "postgresql+psycopg2://%s/%s" % DB_CONFIG

DB_ECHO = True
DB_AUTOCOMMIT = True


import logging
if APP_ENV == 'dev':
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO
