import sys
sys.path.append('../')

from datetime import datetime
from astral import Sun

sun = Sun()
sun_times = sun.get_event_times(datetime.now(), 47.16222, 27.58889)

for event, time in sun_times.items():
    print('%s: %s' % (event, time))