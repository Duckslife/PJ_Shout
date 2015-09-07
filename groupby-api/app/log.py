# -*- coding: utf-8 -*-

import logging

from app import config

logging.basicConfig(level=config.LOG_LEVEL)
LOG = logging.getLogger('TallyBy')


def get_logger():
    return LOG