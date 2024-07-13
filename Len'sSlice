#Lists -- Len's Slice -- Cyb3r_Fr0g -- 7/13/24

# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#combine lists
pizza_and_prices = [list(pair) for pair in zip(prices, toppings)]
#print(pizza_and_prices)

pizza_and_prices.sort()
#print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.remove(pizza_and_prices[-1])
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print("\nOur Three Cheapest Slices\n" + str(three_cheapest))

#the mice left a 5 star review
reviews = [5, 3, 4, 5, 5, 4, 1]
stars = (sum(reviews) / len(reviews)) 
print(f"\nOur raiting is {stars:.2f}/5 stars")
