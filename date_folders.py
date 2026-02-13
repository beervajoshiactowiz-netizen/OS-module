import os
from datetime import datetime,timedelta

# os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{datetime.now().date()}")

n=datetime.now().date()

last_date=datetime(2026,12,31)
t=last_date.date()

days=(t-n).days
print(days)

for i in range(days):
    n+=timedelta(days=1)
    print(n)
    os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{n}")

