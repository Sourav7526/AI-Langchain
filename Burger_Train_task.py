#1 PROBLEM

# 🚆 Railway Ticket Booking System

# Problem Statement:
# You are tasked with creating a simple railway ticket booking system for a fictional railway 
# company called CodeRail. The system should ask users for their age, travel class, and whether 
# they want a meal included. Based on this input, the system will calculate and display the total
#  ticket price.

# 🎯 Requirements:
# 1. Ask the user for their name and age. ✅
# 2. Ask them to choose a class:
# ⿡ First Class – ₹1500
# ⿢ Second Class – ₹1000
# ⿣ Sleeper Class – ₹500  ✅
# 3. If the passenger is under 5 years old, the ticket is free.
# 4. If the passenger is a senior citizen (60+), apply a 20% discount.
# 5. Ask if they want to add a meal:
# Yes – ₹200 extra
# No – No extra charge
# 6. Finally, print the passenger details and the final ticket price.

#------------------------------------------------------------#
# 💻 Sample Output:

# Welcome to CodeRail Railway Booking System 🚆

# Enter your name: Rahul
# Enter your age: 65
# Choose travel class:
# 1. First Class
# 2. Second Class
# 3. Sleeper Class
# Enter choice (1/2/3): 1
# Do you want to add a meal? (yes/no): yes

# ----- Ticket Summary -----
# Passenger Name: Rahul
# Age: 65
# Class: First Class
# Meal Added: Yes
# Final Price: ₹1400.0
# Enjoy your journey! 🎉

#------------------------------------------------------------#
# Solution :

# name=str(input("enter your name"))
# age=int(input("enter your age"))

# print("choose a class")
# print("1. first class=1500")
# print("2. second class=1000")
# print("3. sleeper class=500")

# choice=int(input("enter your choice(1/2/3): "))
# if choice == 1:
#     ticket_price = 1500
#     travel_class = "First Class"
# elif choice == 2:
#     ticket_price = 1000
#     travel_class = "Second Class"
# elif choice == 3:
#     ticket_price = 500
#     travel_class = "Sleeper Class"

# if age<5:
#     ticket_price = 0
# elif age>=60:
#     ticket_price = ticket_price * 0.8  


# meal = input("Do you want to add a meal? (yes/no): ").lower()

# if meal == "yes":
#     ticket_price += 200
#     meal_status = "Meal Included"
# else:
#     meal_status = "No Meal"

# print("------TICKET SUMMARY-------")
# print("passenger name:",name)
# print("age:",age)
# print("travel class",travel_class)
# print("meal status",meal_status)
# print("final price",float(ticket_price))
# print("Enjoy your journey! 🎉")



#2 problem

# 🧠Burger King has launched a self-order kiosk where customers can place their orders using a Python-based system. 
# Your task is to build a simple Burger King order system in Python. The system should:
# - Display a menu with 3 items and their prices.
# - Let the user choose what they want to order and how many.
# - Ask the user if they have a 

# coupon code

# .
# - If the user enters a valid coupon code, apply the discount.
# - Display the final bill with or without discount applied.




# 🧾MENU


#   Item                                                             Price (₹)

# 1. Whopper Burger                                    ₹150
                                


# 2. Crispy Veg                                         ₹100                                   



# 3. Chicken Wings                                  ₹120                                







# 🎟️


# Code                                                               Discount

# KING50                                                         50% off                                                        

# BK20                                                         ₹20 off total                                                        


# NOCOUPON                                                  No discount




# 🎯

# Use if-else statements to check coupon codes.

# Calculate total price based on the quantity.

# Apply the discount accordingly.

# Print a at the end.

#--------------------------------------------------------------------------#
# Output:

# Welcome to Burger King 🍔!


# Menu:

# 1. Whopper Burger - ₹150
# 2. Crispy Veg - ₹100 
# 3. Chicken Wings - ₹120 
# Enter the item number (1/2/3): 1

# Enter quantity: 2 
# Do you have a coupon code? (yes/no): yes

# Enter your coupon code: KING50 
# Applying coupon...
# Original Price: ₹300 
# Discount Applied: 50% 
# Final Price: ₹150 
# Thanks for ordering at Burger King! 🍟


#--------------------------------------------------------------------------#
# Solution:

print("Welcome to Burger King 🍔!")
print("menu")
print("1. Whopper Burger - ₹150")
print("2. Crispy Veg - ₹100 ")
print("3. Chicken Wings - ₹120 ")
choice=int(input("enter choice 1/2/3 :"))
quantity=int(input("Enter Quantity"))
if choice==1:
    price=150
    itemname="Whopper Burger"
elif choice==2:
    price=100
    itemname="Crispy Veg "
elif choice==3:
    price=120
    itemname="Chicken wings"
else:
    print("nothing added")
bill=price*quantity
discount=0
coupon=input("Do you have a coupon code? (yes/no):" )
if coupon == "yes":
    print("APPLYING COUPON......")
    code = input("Enter your coupon code: enter in capital letters")
    if code == "KING50":
        discount = bill * 0.5
        print("Discount Applied: 50%")
        coupon_status="YES"
    elif code == "BK20":
        discount = 20
        print("Discount Applied: ₹20")
        coupon_status="YES"
    elif code == "NOCOUPON":
        print("No discount applied")
    
else:
    print("No coupon applied")
    coupon_status="NO"

final_price = bill - discount
print("------BILL DETAILS---------")
print("Item:", itemname)
print("Quantity:", quantity)
print("coupon applied ",coupon_status)
print("Final Price: ₹", final_price)
print("Thanks for ordering at Burger King! 🍟")