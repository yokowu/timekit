from time import time, mktime
from datetime import datetime, timedelta

from .parser import parse


class TimeKit:

    def __init__(self, d):
        self._d = d

    def __repr__(self):
        return '<%s [%s]>' % (self.__class__.__name__, self._d.isoformat())

    def __getattr__(self, item):
        """支持获取datetime 对象的属性"""

        if hasattr(self._d, item):
            return getattr(self._d, item)
        msg = 'Clock instance has no attribute "{item}"'.format(item=item)
        raise AttributeError(msg)

    @property
    def timestamp(self):
        return float(mktime(self._d.timetuple()))

    def strftime(self, fmt='%Y-%m-%d %H:%M:%S'):
        return self._d.strftime(fmt)

    @classmethod
    def fromtimestr(cls, timestr):
        d = parse(timestr)
        return cls(d)

    @classmethod
    def now(cls):
        d = datetime.now()
        return cls(d)


    @classmethod
    def utcnow(cls):
        d = datetime.utcnow()
        return cls(d)
