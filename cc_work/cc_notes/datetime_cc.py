from datetime import datetime


#获取当前时间
now_c = datetime.now()
print(type(now_c))

#获取指定时间
dt = datetime(2020,11,25,00,00,00)
print(dt)

#datetime时间转换成timestamp时间戳
print(dt.timestamp())

#timestamp时间戳转成成datetime
tc = 1429417200.0
print(datetime.fromtimestamp(tc))

#str转换成datetime
str_c = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(type(str_c))

#datetime转换成str
now_c2 = now_c.strftime('%Y-%m-%d %H:%M:%S')
print(type(now_c2))

