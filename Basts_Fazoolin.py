#Classes -- Basta Fazoolin'-- Cyb3r_Fr0g -- 8/29/24


#class function for menus
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  #prints menu and time it is served
  def __repr__(self):
    return f"The {self.name} menu is available from {self.start_time} to {self.end_time}".format(self.name, self.start_time, self.end_time)
  #Calculates total costs
  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    total = 0
    for item in self.purchased_items:
      
      total += self.items[item]
    return total

#Menus and times they are served
brunch = Menu("brunch", {
'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11 , 16 )
early_bird = Menu("early_bird", {
'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 3, 18 )
dinner = Menu("dinner", {
'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21 )

arepas_menu = Menu("Take a' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 22)

#Testing for menus
print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


#Franchises class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return f"The resturant is located at {self.address}".format(self.address)
  #checks to see if the menu is availible at any given time
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
      
#Define the locations
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

print(flagship_store.available_menus(17))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

company = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
newcompany = Business( "Take a' Arepa", arepas_place)
