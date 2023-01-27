from datetime import datetime

def main(amro_date):
    date_str= str(amro_date)
    date = datetime.strptime(date_str,"%Y%m%d")
    return date