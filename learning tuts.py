# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)

# weight = int(input('Weight: ') )
# unit = input('(L)bs or (K)g: ')

# if unit.upper() == 'L':
#     converted_weight = (weight)* 0.45
#     print(f'your weight is {converted_weight} kilos')

# else:
#     converted_weight = (weight) // 0.45
#     print(f'your weight is {converted_weight} pounds')

 


#formatted strings
# frist_name = "John"
# last_name = "Doe"
# msg = f"{frist_name} {last_name} is already in the bus."
# print(msg)

#Square brackets are used  to get a character and an index in a string
#Assign a number to represent each course in a school(1-10)
# number = int(input('Enter your Number: '))
# Courses = ['Math', 'Music' , 'English'  ,'Business', 'Sciences', 'History', 'Arts', 'design', 'Drama', 'Pysics']
# if 1 <= number <= 10:
#    course = Courses[number - 1]
#    print(course)

# #String Methods
# #To calculate the number of characters in a string we can use a built in function called (len)
# len()
# course.upper() #For converting a string to upper case
# course.lower() #For converting a string to lower case
# course.capitalize() #For converting the first letter of a string to upper case
# course.title() #For converting the first letter of a string to upper case and the rest to lower case
# course.isupper() #For checking if a string is upper case
# course.islower() #For checking if a string is lower case
# course.istitle() #For checking if a string is title case
# course.find() #Returns the index of a character or sequence of characters
# course.replace() #For replacing characters and words in a string
# '...' in course #characters in a string

# #if statement
# #price of a house is $1000000.00. if buyer has good credit, they need to put down 10% otherwise they need to put down 20%. Print the downpayment
# price_of_house = 1000000
# has_good_credit = True

# if has_good_credit:
#     downpayment = price_of_house * 0.10
#     print(f'Downpayment is ${downpayment}')
# else:
#     downpayment = price_of_house * 0.20
#     print(f'Downpayment is {downpayment}')

#Logical (and) operators
#if applicant has high income AND good credit then he/she is Eligible for a loan
 
#Defining boolean variables
# has_high_income = True

# has_good_credit = True

# if has_high_income and has_good_credit:
#     print('Eligible for a loan')

# #Logical (or) operators
# has_high_income = False

# has_good_credit = True

# if has_high_income or has_good_credit:
#     print('Eligible for a loan')

# #Logical (not) operators

# has_high_income = False

# has_good_credit = True

# if not has_high_income and  has_good_credit:
#     print('Eligible for a loan')

#Comparison operators(<,>,<=,>=,==,!=,in,not in)
#if name is less than 3 characteers long name must be at least 3 characters otheerwise if it's more than 50 characters long name can be a maximum of 50 characters otherwise
# name looks good!

# name = input('What is your name?:')

# if len(name) < 3:
#     print(f'{name} must be at least 3 characters long')
# elif len(name) > 50:
#     print(f'{name} can be a maximum of 50 characters')
# elif len(name) >= 3 and len(name) <= 50:
#     print(f'{name} looks good!')

  if not user_cart:
        print("Your cart is empty. Nothing to checkout.")
        return

    total_cart_price = sum(store_items[next(i for i, x in enumerate(store_items) if x["name"] == item)]["price"] * quantity for item, quantity in user_cart.items())
    print(f"Total Cart Price: ${total_cart_price:.2f}")
    user_account_balance = float(input("Enter amount to pay: "))
    if user_account_balance >= total_cart_price:
        change = user_account_balance - total_cart_price
        print(f"Thank you for your purchase! Your change: ${change:.2f}")
        user_cart.clear()  # Empty the cart after successful checkout
    else:
        print("Insufficient balance. Please add more funds or remove items from your cart.")
