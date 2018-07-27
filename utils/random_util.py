# -*- coding: UTF-8 -*-

from datetime import datetime
import random

def gen_current_timestamp_str():
    current = datetime.now()
    return current.strftime('%Y%m%d%H%M%S%f')

def set_random_number():
    nuber = str(random.randint(1,9999))
    return nuber