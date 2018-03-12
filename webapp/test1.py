# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    d1=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    