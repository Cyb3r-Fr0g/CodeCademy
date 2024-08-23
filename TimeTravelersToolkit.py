#Modules -- Time Traveler's Toolkit -- Cyb3r_Fr0g -- 8/23/24

#This function was stored in a seperate file named custom_module.py 
def generate_time_travel_message(year, destination, cost):
  return (f"You have arived at {destination} in the year {year}. The total cost of this trip costs ${cost:.2f}.")

#Main file starts here

import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module

#time traveled to
year = randint(1800, 2100)
month = randint(1, 12)
day = randint(1, 29)

destination = ["europe", "North America", "Africa"]
date = (dt.date.today())
time = (dt.datetime.now().time())

#print (date, time)
#multiplier for cost
base = Decimal('4')
#calculation for time traveled
time_traveled = abs((dt.datetime.now() - dt.datetime(int(year), int(month), int(day))))
#Cost calculation
cost = (float(base) * ((time_traveled.total_seconds() /60) /24))
#print(time_traveled)
#print(cost)
# Final function that prints the time travel message.
print(custom_module.generate_time_travel_message(year, choice(destination), cost))
