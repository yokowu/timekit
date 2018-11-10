import timekit


t = timekit.get('2018-01-23 23:34:34')
t2 = timekit.utcnow()
print(t2.strftime())
