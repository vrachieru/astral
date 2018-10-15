from math import sin, cos, asin, acos

from .constants import PI, RAD, J0, J2000
from .utils import from_julian, to_days, declination

class Sun:

    _TIMES = [
        [-0.833, 'sunrise',         'sunset'       ],
        [  -0.3, 'sunrise_end',     'sunset_start' ],
        [    -6, 'dawn',            'dusk'         ],
        [   -12, 'nautical_dawn',   'nautical_dusk'],
        [   -18, 'night_end',       'night'        ],
        [     6, 'golden_hour_end', 'golden_hour'  ]
    ]

    def _mean_anomaly(self, days):
        return RAD * (357.5291 + 0.98560028 * days)

    def _ecliptic_longitude(self, mean):
        center = RAD * (1.9148 * sin(mean) + 0.02 * sin(2 * mean) + 0.0003 * sin(3 * mean))
        perihelion = RAD * 102.9372
        return mean + center + perihelion + PI

    def _julian_cycle(self, d, lw):
        return round(d - J0 - lw / (2 * PI))

    def _approx_transit(self, Ht, lw, n):
        return J0 + (Ht + lw) / (2 * PI) + n

    def _hour_angle(self, h, phi, d):
        return acos((sin(h) - sin(phi) * sin(d)) / (cos(phi) * cos(d)))

    def _solar_transit(self, ds, M, L):
        return J2000 + ds + 0.0053 * sin(M) - 0.0069 * sin(2 * L)

    def _get_set(self, h, lw, phi, dec, n, M, L):
        w = self._hour_angle(h, phi, dec)
        a = self._approx_transit(w, lw, n)
        return self._solar_transit(a, M, L)

    def get_event_times(self, date, latitude, longitude):
        lw = RAD * -longitude
        phi = RAD * latitude

        d = to_days(date)
        n = self._julian_cycle(d, lw)
        ds = self._approx_transit(0, lw, n)

        M = self._mean_anomaly(ds)
        L = self._ecliptic_longitude(M)
        dec = declination(L, 0)

        Jnoon = self._solar_transit(ds, M, L)

        result = dict()

        for time in self._TIMES:
            Jset = self._get_set(time[0] * RAD, lw, phi, dec, n, M, L)
            Jrise = Jnoon - (Jset - Jnoon)
            result[time[1]] = from_julian(Jrise)
            result[time[2]] = from_julian(Jset)

        return result
