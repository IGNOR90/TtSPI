from datetime import datetime, date, time

date = datetime.now()
hour = date.hour
minutes = date.minute

if hour == 23 and minutes == 58:
    print("Пора")
else:
    print('Ещё не пора')


