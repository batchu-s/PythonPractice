# Printing current date and time
import datetime
time = datetime.datetime.now()
print("Current Date and Time", end=': ')
print(time.strftime("%Y-%m-%d %H:%M:%S"))