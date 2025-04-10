# lists
cart = ["apples", "bananas", "cherries"]
print(cart)

cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
print(cart)

if "pineapple" in cart:
    cart.remove("pineapple")

cart.pop(3)
print(cart)

#cart.remove() and cart.pop() are interchangeable using val or index respectively
#cart.pop without an index treats list like stack, removing last added value

cart.pop()
print(cart)

cart.reverse()
print(cart)

cart.append("cherries")

cart.sort()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

# cart[start_index:end_index]
fruit_basket = cart[4:]
print(cart)
print(fruit_basket)

squares = []
for i in range(1,10):
    squares.append(i**2) # or (i*i)
print(squares)

squares2 = [x * x for x in range(1,10)]
print(squares2)

values = [34, 27, 95, 18, 36, 21, 64, 50, 77]
even_values = [x for x in values if x % 2 == 0]
print(even_values)

squares = [i * i for i in range(1,10)]
print(squares)

b_items = [i for i in cart if i.startswith("b")]
print(b_items)

inventory = [0]*len(cart)
print(inventory)
inventory[0] = 100

# sets

number_set = set()
number_set = {1,1,2,3,4,0,10,5}
print(number_set)
number_set.add(-10)
print(number_set)

num_list = [1,1,4,5,5,6,6]
no_dups = set(num_list)
print(no_dups)
no_dups = list(no_dups)
print(no_dups)
# set no_dups no longer exists, no_dups is now a list

ns = sorted(number_set)
print(ns)

# dictionary
fav_snacks = {}
fav_snacks = {
    "kathleen" : "tortilla chips", 
    "maggie" : "pretzels", 
    "emily" : "buffalo chicken dip",
    "ava" : "chocolate"
}
print(fav_snacks)

fav_snacks["wade"] = "popcorn"
print(fav_snacks)

print("kathleen's favorite snack is " + fav_snacks["kathleen"])
if "bob" in fav_snacks:
    print("bob's favorite snack is " + fav_snacks["bob"])

for key in fav_snacks: 
    # print(key+"'s favorite food is " + fav_snacks[key])
    print(f"{key}'s favorite food is {fav_snacks[key]}")
    
for key,value in fav_snacks.items():
    print(key,value)

keys = fav_snacks.keys()
values = fav_snacks.values()

fav_snacks["alice"] = ["chips","nuts"]
print(fav_snacks)

