# 1)	Build a program that:
# •	Displays a list of snacks and drinks with item numbers and prices. 
# •	Ask the user to choose items by number in a loop.
# •	 Keeps track of selected items and their prices.
# •	Ends when the user types "done".
# •	Finally prints a receipt showing: List of selected items with prices and total cost
# Step 1: Menu
snacks = ["Kolo", "Chips", "juice","COCA"]
prices = [5, 3, 2,7]

# Step 2: Display menu
print("---- Snack Menu ----")
for i in range(len(snacks)):
    print(str(i+1) + ". " + snacks[i] + " - $" + str(prices[i]))

# Step 3: User adds items to cart
cart = []  # list to store selected snacks
cart_prices = [] # list to store thier prices

while True:
    choice = input("Enter item number to add to cart (or 'done' to finish): ").lower()
    if choice == "done":
        break
    
    choice = int(choice)  # convert input to number
    cart.append(snacks[choice-1]) #convert human-friendly number to list index cause indexing start from 0 and added to cart saves the name
    cart_prices.append(prices[choice-1]) # save the price
# Step 4: Print receipt
total = 0
print("---- Receipt -----")
for i in range(len(cart)):
    print(cart[i] + " - $" + str(cart_prices[i]))
    total += cart_prices[i]

print("Total: $" + str(total))