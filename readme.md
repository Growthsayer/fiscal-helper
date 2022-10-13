The ***Fiscal Calendar Helper*** is a set of fiscal calendar helper functions that enables easy use and navigation of a fiscal calendar in Python 3 projects.

<br>

# **API Reference:** 
- [Installation](#installation)
- [The Fiscal Calendar](#the-fiscal-calendar)
- [Time Offsets](#time-offsets) - Moving between time periods
  - [fiscal.offset()](#fiscaloffset)
  - [fiscal.next()](#fiscalnext)
  - [fiscal.previous()](#fiscalprevious) 
- [Time Conversions](#time-conversions) - Converting between time levels
  - [fiscal.convert()](#fiscalconvert)
- [Parent / Child Time Relationships](#parent--child-time-relationships) - Managing time in with the hierarchy
  - [fiscal.fill_to()](#fiscalfillto)
  - [fiscal.unpack()](#fiscalunpack)
- [More Info](#more-info) - Repo, bugs, license info

<br>

# **Installation**
To use the fiscal helper:
```
from fiscal_calendar_helper import fiscal 
```

<br>

# **The Fiscal Calendar**
The current fiscal calendar is based on the [National Retail Federation](https://nrf.com/)'s 4-5-4 [calendar](https://nrf.com/resources/4-5-4-calendar). In the future, we plan to support other calendars (Gregorian), different starting days of week, and longer time horizons.

The current supported years are 2016 - 2025

<br>

## **Time Levels**

Our fiscal calendar is capable of supportting different levels of the calendar hierarchy. While many of the examples may look similar to the other levels, their structures are not interchangable and mean something specific to that level.

| Level | Description | Example | Data Type |  Relative or Absolute | 
| --- | --- | --- | --- | --- |
| `key` | This is a numeric key for this record and should not be confused with the date itself. This is most likely not what you're looking for. It's a structure holding counts of year, week, and day_of_week as an index starting at 1. For example this key `2023_07_7` actually represents the date 3/18/23 which looks totally different. | `2023_07_7` | `string`| Absolute |
| `week_id` | This is unique id for this fiscal week | `2023_07` | `string`| Absolute |
| `year` | This is the fiscal year. | `2023` | `string`| Absolute |
| `quarter` | This is the fiscal quarter. | `Q1` | `string`| Relative |
| `month` | This is the fiscal month. | `March` | `string`| Relative |
| `week_num` | This is a relative count of the number of weeks in the year. | `7` | `string`| Relative |
| `day_of_week` | This is the day of the week in plain text. | `Saturday` | `string`| Absolute |
| `date` | This is a datetime formatted representation of the fiscal date. | `2023-03-18` | `datetime`| Absolute |
| `date_id` | This is the id for this date. |  `2023_03_18` |`string`| Absolute |

<br>

### **Relative vs Absolute Levels**
Absolute levels mean that this column only uses one value for a specific time period, where as relative levels mean that the value in the column may be repeated over several time periods.

A `week_id` such as `2023_07` is absolute because it will only occur once on the calendar, where as `week_num` such as `7` because that will exist for every year in the calendar.

Most of the time, you'll likely be working with absolute dates only - like finding the starting date for a particular week. But you may also want to compare months (Relative) across several years (Absolute) to create a table where values can be compared directly.

<br>

## fiscal.**calendar**

The actual fiscal calendar is stored as a [pandas](https://pandas.pydata.org) table located at `fiscal.calendar`.

<br>

# **Time Offsets**

All of the time offsets are currently only built to work with `week_id` or `date_id` levels.

<br>

## fiscal.**offset()**
`offset(input, offset)`

<br>

Returns `week_id` or `date_id` offset by specified periods.

```
>>> fiscal.offset('2022_31', 4)
'2022_35'
```
<br>

## fiscal.**next()**
`next(input)`

<br>

Returns the next week or date.
```
>>> fiscal.next('2022_31')
'2022_32'
```
<br>

## fiscal.**previous()** 
`previous(input)`
<br>
Returns the previous week or date.
```
>>> fiscal.previous('2022_31')
'2022_30'
```
<br> 

# **Time Conversions**

Time conversions allow for easy translation between years, weeks, week nums, etc without having to parse strings.


## fiscal.**convert()**
`fiscal.convert(input, inp_level, out_level)`

<br>

The `convert` function takes an input and level type, and output level and converts the value.  If there are multiple valid answers, it will return the first time in the list.

Example: Find the starting date for a fiscal week
```
>>> fiscal.convert('2022_36', 'week_id', 'date')
['2016_02_14', '2016_02_15', '2016_02_16', '2016_02_17']
```

<br>

# **Parent / Child Time Relationships**
Time is structured into a hierarchy, which means that there are parent and child elements in the hierarchy structure. You can read more on [parent-child hierarchies](https://www.ibm.com/docs/en/ida/9.1.2?topic=hierarchies-parent-child) if the concept is unfamiliar.

For our purposes a parent-like level will be any level that contains multiple child elements of the same type. 

**Examples:** 

 - `year` is parent-like to `quarter`
 - `week` is child-like to `quarter`
 - `week` is parent-like to `date` and `date_id`
 - `year` is parent-like to `date`
 - `date` is child-like to `month`

<br>

## fiscal.**fill_to()**
`fill_to(input, child_level = 'date_id', parent_level = 'week_id', direction = 'start')`

<br>

The `fill_to` function takes a child input as a starting point, and then a parent output as a container, and lists the remaining children in that parent. 

Example: Given a date, find the remaining dates in the week.
```
>>> fiscal.fill_to('2016_02_18', 'date_id', 'week_id', 'start')
['2016_02_14', '2016_02_15', '2016_02_16', '2016_02_17']
```

## fiscal.**unpack()**
`unpack(input, parent_level, child_level)`

<br>

The `unpack` function takes in a parent level and returns all the children contained withint it.

Example: Return all dates within a quarter.
```
>>> fiscal.unpack('2016_01', 'week_id', 'date_id')
['2016_02_07', '2016_02_08', '2016_02_09', '2016_02_10', '2016_02_11', '2016_02_12', '2016_02_13']
```
<br>

# **More info**
- Author: Phillip Geltman
- License Type: MIT License
- Github Repo: https://github.com/Growthsayer/fiscal-helper
- Bug Tracker: https://github.com/Growthsayer/fiscal-helper/issues