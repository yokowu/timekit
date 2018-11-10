# timekit Simple, easy-to-use time converter

supports Python3

Installation
------------
```
pip3 install timekit
```

Example
-------

``` {.sourceCode .python}
>>> import timekit
str to timestamp
>>> t = timekit.get('2018-01-01 15:34:34')
>>> t.timestamp
1514792074.0

timestamp to str
>>> t = timekit.get(1514792074)
>>> t.strftime()
'2018-01-01 15:34:34'
>>> t.strftime('%Y-%d-%m')  # You can specify the format
'2018-01-01'

get current time
>>> t = timekit.now()
>>> t.timestamp
1541815100.0
>>> t.strftime()
'2018-11-10 09:58:20'
```
