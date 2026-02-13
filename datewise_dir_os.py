import os
from datetime import datetime,timedelta
current_date=datetime.now().date()
last_date=datetime(2026,12,31).date()

total_days_from_now=(last_date-current_date).days

for i in range(total_days_from_now):
    current_date+=timedelta(days=1)
    os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{current_date}")