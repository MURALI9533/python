from datetime import datetime,timedelta
now=datetime.now()
print(now)
d=now.strftime('%d/%m/%y %H:%M:%S')
print(d)
u_t=now+timedelta(hours=6)
print(u_t)
d=u_t.strftime('%d/%m/%y %H:%M:%S')
print(d)
