"""
Original Authors:
    Gabriel Russell
    Charlie Cornell-Hayes
    Tamyrah Pugh
    Sierra Cuyler

Program Purpose:
    Simulate a restaurant menu, and offer a variety of choices.
    Display the total cost, along with taxes.

License:
    GPL v3
    https://www.gnu.org/licenses/gpl-3.0.en.html
    You should recieve a copy of this license with this program.

Later Authors:
    - Your Name Here -
"""
# Print out a welcome message 
print ("Welcome to our Simulated Menu, please choose an option for ordering: ")
# Record what menu they want to order from
menuChoice = input("1. Entree's\n2. Drinks\n3. Sides\n4. Finish Ordering\n\nYour Choice: ")
# Set variables to keep track of how many of each item they order
burgers = 0
sandwich = 0
spaghetti = 0
water = 0
soda = 0
juice = 0
chips = 0
fries = 0
salad = 0

# Make a while loop, while the customers did not choose to exit the menu
while menuChoice != "4":

    # If the customer chose to look at entrees
    if menuChoice == "1":
        # Display Entree Option and Prices

        print("Burger:                  $5\nChicken Sandwich:        $4\nSpaghetti and Meatballs: $6\n\n")
        # Ask the user what they want to order
        choice = input("What would you like to purchase? 1: Burger, 2: Sandiwch, 3: Spaghetti, 4: Order Nothing\n\nYour Choice:")
        # Accumulate to their order based on what they chose. Use the variables you created earlier.
        if choice == "1":
            burgers += 1
        elif choice == "2":
            sandwich += 1
        elif choice == "3":
            spaghetti += 1
        # Print a thank you message, continue the while loop.
        print("Thank you for looking at our Entree Selection.")

    # If the customer chose to look at drinks,    
    elif menuChoice == "2":
        # Display Drink Options and Prices

        print("Water: FREE\nSoda:  $2\nJuice: $3\n\n")
        #Ask the user what they'd like to order
        choice = input("What would you like to purchase? 1: Water, 2: Soda, 3: Juice, 4: Order Nothing\n\nYour Choice:")
        # Accumulate to their oder based on what they chose. Use the variables you created earlier.
        if choice == "1":
            water += 1
        elif choice == "2":
            soda += 1
        elif choice == "3":
            juice += 1
        # Print a thank you message, continue the while loop
        print("Thank you for looking at our Drinks Selection.")
    # If the user chose to look at sides,
    elif menuChoice == "3":
        # Display Side Options and Prices

        print("Chips: $1\nFries: $1\nSalad: $2")
        # Ask the user what they want to order
        choice = input("What would you like to purchase? 1: Chip, 2: Fries, 3: Salad, 4: Order Nothing\n\nYour Choice:")
        # Accumulate to their order based on what they chose. Use the variables they created earlier.
        if choice == "1":
            chips += 1
        elif choice == "2":
            fries += 1
        elif choice == "3":
            salad += 1
        # Print a thank you message, continue the while loop
        print("Thank you for looking at our Sides Selection.")

    # Make sure the user didn't accidentally pick something other than what you offered in the while loop, let them know
    else:
        print("Incorrect Selection")
        # Incorrect Selection
    # Ask the user if they'd like to continue ordering. This should be your While Loop's Condition, so that it can reset if they choose to keep ordering.
    menuChoice = input("Would you like to reorder? Or finish ordering?\n1. Entree's\n2. Drinks\n3. Sides\n4. Finish Ordering\n\nYour Choice: ")

# Tell them thank you for ordering.
print("Thank you for ordering!")

# Calculate how many of each item they purchased, and the accompanying price.
if burgers > 0:
    print("You ordered " + str(burgers) + " Burgers, Costing $" + str(burgers * 5))
if sandwich > 0:
    print("You ordered " + str(sandwich) + " Chicken Sandwiches, Costing $" + str(sandwich * 4))
if spaghetti > 0:
    print("You ordered " + str(spaghetti) + " servings of Spaghetti and Meatballs, Costing $" + str(spaghetti * 6))
if water > 0:
    print("You ordered " + str(water) + " cups of water, free of charge.")
if soda > 0:
    print("You ordered " + str(soda) + " cups of soda, Costing $" + str(soda * 2))
if juice > 0:
    print("You ordered " + str(juice) + " cups of juice, Costing $" + str(juice * 3))
if fries > 0:
    print("You ordered " + str(fries) + " servings of fries, Costing $" + str(fries))
if chips > 0:
    print("You ordered " + str(chips) + " servings of chips, Costing $" + str(chips))
if salad > 0:
    print("You ordered " + str(salad) + " servings of salad, Costing $" + str(salad * 2))


# Calculate the sub total from each of the items
totalCost = (burgers * 5) + (sandwich * 4) + (spaghetti * 6) + (soda * 2) + (juice * 3) + chips + fries + (salad * 2)
print("Your sub total came to... $" + str(totalCost))
# Calculate the Taxes from the total Cost: 5%, 1%, and 2%, separately, not accumulative.
stateTax = totalCost * 0.05
localTax = totalCost * 0.01
specTax = totalCost * 0.02

# Print out their total taxes and price
print("You pay 5% State Taxes, coming to   $" + "%.02f" % stateTax)
print("You pay 1% Local Taxes, coming to   $" + "%.02f" % localTax)
print("You pay 2% Special Taxes, coming to $" + "%.02f" % specTax)

# Print out their total order cost, with taxes.
print("Your total is... $" + "%.02f" % (totalCost + stateTax + localTax + specTax))
