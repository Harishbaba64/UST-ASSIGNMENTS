### 1. Calculate the cost of the trip
def calculate_trip_cost(kilometers, liters_per_km, price_per_liter):
    total_liters = kilometers * liters_per_km
    total_cost = total_liters * price_per_liter
    return total_cost

kilometers = float(input("Enter kilometers to drive: "))
liters_per_km = float(input("Enter liters-per-kilometer usage of the car: "))
price_per_liter = float(input("Enter price per liter of fuel: "))

trip_cost = calculate_trip_cost(kilometers, liters_per_km, price_per_liter)
print(f"The cost of the trip is: ${trip_cost:.2f}")
```


### 2. Calculate total expenses with a discount
def calculate_total_expenses(quantity, price_per_item):
    total_cost = quantity * price_per_item
    if quantity > 10:
        total_cost *= 0.9
    return total_cost

quantity = int(input("Enter the quantity of items: "))
price_per_item = float(input("Enter the price per item: "))

total_expenses = calculate_total_expenses(quantity, price_per_item)
print(f"The total expenses are: ${total_expenses:.2f}")
