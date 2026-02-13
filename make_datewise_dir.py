import os
from datetime import datetime,timedelta

def make_dir(end_date,start_date=datetime.now().date()):

    total_days_from_now=(end_date-start_date).days

    for i in range(total_days_from_now):
        start_date+=timedelta(days=1)
        os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{start_date}")

last_date_input=input("enter in YYYY-MM-DD format: ")
last_date=datetime.strptime(last_date_input,"%Y-%m-%d").date()

make_dir(last_date)
