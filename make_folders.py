import os
from datetime import datetime, timedelta

def make_dir(first_date):
    first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    year = first_date.year
    last_date=datetime(year,12,31).date()
    total=(last_date-first_date).days
    try:
        for i in range(total):
            first_date+=timedelta(days=1)
            os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{first_date}")
        print("folders formed sucessfully")
    except FileExistsError:
        print("Folders already exist")

start_date_input=input("Enter starting date in yyyy-mm-dd format:")
make_dir(start_date_input)