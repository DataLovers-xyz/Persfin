def main(amro_date):
    date_str= str(amro_date)
    date = date_str[6:]+"/"+date_str[4:6] +"/"+date_str[:4]
    return date