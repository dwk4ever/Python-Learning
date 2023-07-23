# my online grocery store:

import colorama
from colorama import Fore, Back, Style
colorama.init()

 
store_items = [
    {
        "name": "cheese",
        "price": 10.00
         
    },
    {
        "name": "egg",
        "price": 2.00 
    },
    {
        "name": "bread",
        "price": 7.00 
        
    },
    {
        "name": "milk",
        "price": 8.00 
    },
    {
        "name": "can of tomatoes",
        "price": 8.00 
    },
    {
        "name": "soap",
        "price": 3.00 
    },
    {
        "name": "pound of chicken",
        "price": 20.00
    },
    {
        "name": "toothbrush",
        "price": 2.00 
    
    },
    {
        "name": "box of sugar",
        "price": 15.00 
    },
    {
        "name": "tin of milo",
        "price": 10.00 
    },
]

 

#function to display items in the store
print(Fore.LIGHTYELLOW_EX + "Available items in the store: ")
for i, item in enumerate(store_items):
    item_name = item["name"]
    item_price = item["price"]
    print(Fore.MAGENTA + f"{i+1}. {item_name} - Ghc{item_price:.2f}")
 


user_input = 0
user_cart = {}


#Main program loop
while True:
    print(Fore.LIGHTYELLOW_EX+ "**** Welcome to my online grocery store! *****")
    print(Fore.LIGHTBLUE_EX + "How may I help You today?,Please select an option:")
    user_input= int(input(Fore.LIGHTCYAN_EX + """ 
         1. Add to cart
         2. Remove  from cart
         3. View my cart
         4. Checkout
         5. About us
         6. Exit store\n\n
         Select an option: """))
    
    #Add item from store items to user_cart
    if user_input == 1:
         item_number = int(input(Fore.BLUE + "Enter the item number: "))
         if item_number > 0 and item_number <= len(store_items):
             item_name = store_items[item_number-1]["name"]
             item_price = store_items[item_number-1]["price"]
                
             if  item_name in user_cart:
                   
                   confirm = input(Fore.LIGHTRED_EX + f"Item {item_name.upper()} already in your cart. Would you like to add it again? (yes/no): ")
                   if confirm.lower() == "yes":
                        user_cart[item_name] += 1
                        print(Fore.LIGHTGREEN_EX + f"You have added another {item_name.upper()}  to your cart!")

                   else:
                        print(Fore.LIGHTRED_EX + "item not added to your cart!")
             else:
                  user_cart[item_name] = 1
                  print(Fore.GREEN + f"You have added {item_name} to your cart!")
         else:
              print(Fore.LIGHTRED_EX + f"Item {item_number} does not exist in the store!")



    #Remove   item from user_cart
    if user_input == 2:
         item_number = int(input(Fore.BLUE + "Enter the item number: "))
         if item_number > 0 and item_number <= len(store_items):
             item_name = store_items[item_number-1]["name"]
             item_price = store_items[item_number-1]["price"]
             
             if item_name in user_cart:
                  
                 confirm = input(Fore.LIGHTRED_EX + f"There are {user_cart[item_name]} of {item_name}. Do you want to remove all? (yes/no): ")
                 if confirm.lower() == "yes":
                      del user_cart[item_name]
                      print(Fore.LIGHTGREEN_EX + f"You have removed all of {item_name} from your cart!")
                     
                 else:
                      quantity = int(input(Fore.LIGHTRED_EX + f"How many {item_name} do you want to remove?: "))
                      if 1 <= quantity <= user_cart[item_name]:
                           user_cart[item_name] -= quantity
                           print(Fore.LIGHTGREEN_EX + f"You have removed {quantity} {item_name} from your cart!")
                      else:
                           print(Fore.LIGHTRED_EX + f"{quantity} {item_name} is not in your cart!")
             else:
              print(Fore.LIGHTRED_EX + f"Item {item_number} does not exist in the store!")


    #View my cart
    if user_input == 3:
         if not user_cart:
              print(Fore.LIGHTRED_EX + "Your cart is empty!")
         else:
              print(Fore.WHITE + "Items in your cart:")
              total_cart_price = 0
              for item, quantity in user_cart.items():
                  item_info = next((x for x in store_items if x["name"] == item), None)
                  if item_info:
                            item_name = item_info["name"]
                            item_price = item_info["price"]
                            total_price = quantity * item_price
                            total_cart_price += total_price
                            print(Fore.GREEN + f"{item_name.capitalize()} - Quantity: {quantity} - Price per item: Ghc{item_price:.2f} - Total Price: Ghc{total_price:.2f}")
              print(Fore.MAGENTA + f"\nTotal cart price: Ghc{total_cart_price:.2f}")


    # User Checkout
    if user_input == 4:
         if not user_cart:
              print("Your cart is empty. Nothing to checkout.")
        
         else:
            total_cart_price = sum(store_items[next(i for i, x in enumerate(store_items) if x["name"] == item)]["price"] * quantity for item, quantity in user_cart.items())
            print(Fore.MAGENTA + f"Total Cart Price: Ghc{total_cart_price:.2f}")
            user_account_balance = float(input(Fore.LIGHTBLUE_EX + f"Enter amount to pay: "))
            if user_account_balance >= total_cart_price:
                    change = user_account_balance - total_cart_price
                    print(Fore.GREEN+f"Thank you for your purchase!\n Your change: Ghc{change:.2f}")
                    user_cart.clear()  # Empty the cart after successful checkout
            else:
                print("Insufficient balance. Please add more funds or remove items from your cart.")

    #About us
    if user_input == 5:
        print(Fore.LIGHTWHITE_EX + """ This is an online grocery store. It is a simple shopping cart system CREATED BY DERRICK WIAFE KISSI for users to shop ,keep track of their items
        and also self checkout of their cart. You can add items to your cart, remove items from your cart, view your cart, and checkout""")


    #Exit store
    if user_input == 6:
        print(Fore.LIGHTRED_EX + "Thank you for using our online grocery store!\n Your items will be delivered to you soon")
        break


             
        

                
                  
        

            

 


    
 
             
      
        

