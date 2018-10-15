<p align="center">
    <img src="https://user-images.githubusercontent.com/5860071/46950160-7d3dc880-d08c-11e8-829a-e12cadcf0600.gif" width="200px" />
    <br/>
    <a href="https://github.com/vrachieru/astral/releases/latest">
        <img src="https://img.shields.io/badge/version-1.0-brightgreen.svg?style=flat-square" alt="Version">
    </a>
    <a href="https://travis-ci.org/vrachieru/astral">
        <img src="https://img.shields.io/travis/vrachieru/astral.svg?style=flat-square" alt="Version">
    </a>
    <br/>
    Calculate things that happen beyond the clouds
</p>

## Install

```bash
$ pip3 install git+https://github.com/vrachieru/astral.git
```
or
```bash
$ git clone https://github.com/vrachieru/astral.git
$ pip3 install ./astral
```

## Usage

```python
from datetime import datetime
from astral import Sun

sun = Sun()
sun_times = sun.get_event_times(datetime.now(), 47.16222, 27.58889)

for event, time in sun_times.items():
    print('%s: %s' % (event, time))
```

## Acknowledgements

Calculations are based on http://aa.quae.nl/en/reken/zonpositie.html formulas.

## License

MIT