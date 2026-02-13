import os
from datetime import datetime,timedelta

def make_dir(start_date,end_date):

    total_days_from_now=(end_date-start_date).days

    for i in range(total_days_from_now):
        start_date+=timedelta(days=1)
        os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{start_date}")

current_date=datetime.now().date()
last_date=datetime(2026,12,31).date()

make_dir(current_date,last_date)