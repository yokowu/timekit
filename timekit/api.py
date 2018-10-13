from .factor import TimeKitFactor
from .timekit import TimeKit


_timekit_factor = TimeKitFactor(TimeKit)


def get(timestr):
    return _timekit_factor.get(timestr)