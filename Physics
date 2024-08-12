#Functions -- Getting Ready For Physics Class -- Cyb3r_Fr0g -- 8/11/24

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

#Temp calculations

# F to C
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

# C to F
def c_to_f(c_temp):
  f_temp = c_temp * (5/9) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

#Force calculations

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)


print("The GE train supplies " + str(train_force) + " Newtons of force")

#Energy Calculations

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
