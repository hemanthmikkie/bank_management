# import datetime
# print(datetime)
# print(dir(datetime))
# from datetime import date, datetime, time, timedelta
# print(datetime.now())
# print(date.today())
# print(datetime.now().time())




#timedelta: time difference
# now to bday days difference
# bday = date(2005,8,4)
# print(type(bday))
# days=(date.today () - bday)
# years=days/365.25
# print(years)




#date and time valdity netfilx
# sub_da=date.today()
# print(sub_da)
# val=30
# expi_da=sub_da+timedelta(days=30)  # valid for 30 days days=val
# print(expi_da)




# employee login time
# login_time=time(10,0,0)
# emp_log=time(10,15,0)
# print(emp_log>login_time)

# login_time=datetime(year=2025, month=10, day=1, hour=10, minute=0, second=0)
# emp_log=datetime(year=2025, month=10, day=1, hour=10, minute=15, second=0)
# grace_time=login_time+timedelta(minutes=15)
# print(grace_time)
# print(emp_log>grace_time)


# st=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(st)


# date=datetime(1947,8,14,0,0,)
# print(date)



# st=datetime.now().strftime("%y-%B-%d %H:%M:%S")
# print(st)





# import datetime
# new = datetime.date(2027, 1, 1)
# print(datetime.date.today() - new)



