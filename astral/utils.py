from time import mktime
from datetime import datetime
from math import sin, cos, asin

from .constants import DAY_MS, E, J1970, J2000

# time conversions
def to_julian(date):
    return (mktime(date.timetuple()) * 1000) / DAY_MS - 0.5 + J1970

def from_julian(j):
    return datetime.fromtimestamp(((j + 0.5 - J1970) * DAY_MS) / 1000.0)

def to_days(date):   
    return to_julian(date) - J2000

# general utilities for celestial body position
def declination(l, b):    
    return asin(sin(b) * cos(E) + cos(b) * sin(E) * sin(l))