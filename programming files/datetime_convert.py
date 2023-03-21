from datetime import datetime

#Create string for date and time
date_str = "2022-03-17 10:45:30"
#Create date object using string above
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
#Format the date and time
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

print(formatted_date)
