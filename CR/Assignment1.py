# QUESTION 1

# num = int(input("Enter month number"))
# if num == 1:
#     print("january")
# elif num == 2:
#     print("february")
# elif num == 3:
#     print("march")
# elif num == 4:
#     print("april")
# elif num == 5:
#     print("may")
# elif num == 6:
#     print("june")
# elif num == 7:
#     print("july")
# elif num == 8:
#     print("august")
# elif num == 9:
#     print("september")
# elif num == 10:
#     print("october")
# elif num == 11:
#     print("november")
# elif num == 12:
#     print("december")
# else:
#     print("invalid month")


# QUESTION 2

# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# #1.
# print(num1 == num2)
# #2.
# if num1 > num2:
#     print("first number is bigger")
# elif num2 > num1:
#     print("second number is bigger")
# else:
#     print("both are equal")

# #4.
# if num1>num2:
#     for i in range(5):
#         print("kanan")
# elif num1<num2:
#     for i in range(3):
#         print("kashyap")


#QUESTION 3
# str1 = input("enter first string")
# str2 = input("enter second string")
# print(str1 == str2)
# print(str1 is str2)


#QUESTION 4
# str1 = input("Enter first number: ")
# str2 = input("Enter second number: ")
# n1 = int(str1)
# n2 = int(str2)
# print(n1 is n2)


#QUESTION 5
# n = int(input("enter a number"))
# sum = 0
# for i in range(1,n+1):
#     sum=sum + i
# print("total is ",sum)


#QUESTION 6
# n = int(input("Enter a number"))
# for i in range(1,n+1):
#     if i%2 == 0:
#         print(i)


#QUESTION 7
# name=str(input("enter your name"))
# age=int(input("enter your age"))
# ticket_price =0

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


# meal = input("Do you want to add a meal? (yes/no): ")

# if meal == "yes":
#     ticket_price += 200
#     meal_status = "Meal Included"
# else:
#     meal_status = "No Meal"

# print("------TICKET SUMMARY-------")
# print("passenger name:",name)
# print("age:",age)
# print("meal status",meal_status)
# print("final price",float(ticket_price))
# print("Enjoy your journey! 🎉")


# #QUESTION 8
# print("Welcome to Burger King 🍔!")
# print("menu")
# print("1. Whopper Burger - ₹150")
# print("2. Crispy Veg - ₹100 ")
# print("3. Crispy Veg - ₹120 ")
# choice=int(input("enter choice 1/2/3 :"))
# quantity=int(input("Enter Quantity"))
# if choice==1:
#     price=150
#     itemname="Whopper Burger"
# elif choice==2:
#     price=100
#     itemname="Crispy Veg "
# elif choice==3:
#     price=120
#     itemname="Chicken wings"
# else:
#     print("nothing added")
# bill=price*quantity
# discount=0
# coupon=input("Do you have a coupon code? (yes/no):" )
# if coupon == "yes":
#     print("APPLYING COUPON......")
#     code = input("Enter your coupon code: enter in capital letters")
#     if code == "KING50":
#         discount = bill * 0.5
#         print("Discount Applied: 50%")
#         coupon_status="YES"
#     elif code == "BK20":
#         discount = 20
#         print("Discount Applied: ₹20")
#         coupon_status="YES"
#     elif code == "NOCOUPON":
#         print("No discount applied")
    
# else:
#     print("No coupon applied")
#     coupon_status="NO"

# final_price = bill - discount
# print("------BILL DETAILS---------")
# print("Item:", itemname)
# print("Quantity:", quantity)
# print("coupon applied ",coupon_status)
# print("Final Price: ₹", final_price)
# print("Thanks for ordering at Burger King! 🍟")