#Control Flow -- Sal's Shipping -- Cyb3r_Fr0g -- 7/10/24

weight = 41.5
PPP = 1.00
Amazon1Day = 125.00
#Ground Shipping calculations
#print(f"Cost for amazon overnight ${Amazon1Day:.2f}")
if weight <= 2:
  PPP = 1.50

elif weight <= 6:
  PPP = 3.00
 
elif weight <= 10:
  PPP = 4.00

else:
  PPP = 4.75


#Drone Shipping

if weight <= 2:
  PPD = 4.50
elif weight <= 6:
  PPD = 9.00
elif weight <= 10:
  PPD = 12.00
else:
  PPD = 14.25

#Quick maths for ground calc
gcost = (weight * float(PPP) + 20)
#print(f"Ground shipping rates ${gcost:.2f}")

#Quick maths for drone calc
dcost = (weight * int(PPD))
#print(f"Drone shipping rates ${dcost:.2f}")


#Sort Feature (Optional by authority of Cyb3r-Fr0g)
#Cost List for sort

costs = {
       "Ground Shipping" : gcost,
       "Drone Shipping" : dcost,
       "Ground Premium Shipping" : Amazon1Day
}

#Sort
sorted_costs = sorted(costs.items(), key=lambda x: x[1],)
#Credit AI Assistant

#Print
for shipping_method, cost in sorted_costs:
  print(f"{shipping_method}:${cost:.2f}")
