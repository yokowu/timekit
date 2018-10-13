# -*- coding: utf-8 -*-
import re 
from datetime import datetime


class Parser:

    def __init__(self):
        self._d = datetime.now()

    def parse(self, timestr):
        if isinstance(timestr, str):
            self._handle_datestr(timestr)
        if isinstance(timestr, (int, float)):
            self._handle_datestamp(timestr)
        return self._d

    def _handle_datestamp(self, timestamp):
        self._d = datetime.fromtimestamp(timestamp)

    def _handle_datestr(self, timestr):
        timestr = timestr.strip()
        stamp_pattern = r'(\d+)(\.\d+)?$'
        stamp_reg = re.match(stamp_pattern, timestr)
        if stamp_reg:
            self._handle_datestamp(float(stamp_reg.group()))

        date_pattern = r'(\d{2,4})[-/\.]?(\d{1,2})[-/\.]?(\d{1,2})$'
        date_reg = re.match(date_pattern, timestr)
        if date_reg:
            year = int(date_reg.group(1))
            month = int(date_reg.group(2))
            day = int(date_reg.group(3))
            self._check_date_values(year, month, day)
            self._d = datetime(year=year, month=month, day=day)

        datetime_pattern = r'(\d{2,4})[-/\.]?(\d{1,2})[-/\.]?(\d{1,2})[T\s]' \
                            '(\d{2}):(\d{2}):(\d{2})?'
        datetime_reg = re.match(datetime_pattern, timestr)
        if datetime_reg:
            year = int(datetime_reg.group(1))
            month = int(datetime_reg.group(2))
            day = int(datetime_reg.group(3))
            hour = int(datetime_reg.group(4))
            minute = int(datetime_reg.group(5))
            second = int(datetime_reg.group(6))
            self._check_date_values(year, month, day)
            self._check_time_values(hour, minute, second)
            self._d = datetime(year=year, month=month, day=day, hour=hour,
                                minute=minute, second=second)

    def _check_time_values(self, hour, minute, second):
        if hour < 0 or hour > 23:
            raise ValueError('Please enter the correct time!')
        if minute < 0 or minute > 60:
            raise ValueError('Please enter the correct time!')
        if second < 0 or second > 60:
            raise ValueError('Please enter the correct time!')

    def _check_date_values(self, year, month, day):
        if month < 1 or month > 12:
            raise ValueError('Please enter the correct month!')
        if day < 1 or day > 31:
            raise ValueError('Please enter the correct number of days!')


def parse(timestr):
    p = Parser()
    d = p.parse(timestr)
    return d
