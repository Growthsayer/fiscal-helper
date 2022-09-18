# Fiscal Calendar Helper

This helper function is based on the National Retail Federations 4-5-4 calendar for Python 3.

## Key features: 
- Offset a date or week
- Translate a date to the fiscal week and vice versa

To install
```
pip install git+https://github.com/Growthsayer/fiscal-helper.git
```

To start a new fiscal helper:
```
import Fiscal_Helper from fiscal_helper
fiscal = Fiscal_Helper()
```

## Fiscal Offsets
```
>>> fiscal.offset('2022_31', 4)
'2022_35'
```

## Fiscal next / previous
Returns the next or previous week or date
```
>>> fiscal.next('2022_31')
'2022_32'

>>> fiscal.previous('2022_31')
'2022_30'
```