# Create a simple that program that allows users to create a todo list
import colorama
from colorama import Fore, Back, Style

colorama.init()



todo_list = []
user_input = 0
#Display the user current todo list
if len (todo_list) == 0:
  print(Fore.RED + "No to-dos yet!")
else:
  print(Fore.GREEN + "To-dos:")
  for todo in todo_list:
    print(Fore.BLUE + todo)

#main program loop 
while True:

  print(Fore.GREEN + "*****Derrick To-Do List******")
  user_input = int(input(Fore.BLUE + """ What would you like to do?
1. Create a new todo
2. Delete a todo
3. Edit a todo
4. List all todos
5. Exit\n\n
Select option: """))
  
  if user_input == 1:
    user_input = input("Enter todo item: ")
    if user_input in todo_list:
      print(Fore.RED + "Todo already exists!")
    else:
      todo_list.append(user_input)
      print(Fore.GREEN + "Todo added successfully!")

  elif user_input == 2:
    if len (todo_list) == 0:
      print(Fore.RED + "No todo's yet!")
    else:
      todo_index = int(input(Fore.RED + "Which todo would you like to delete?: ")) -1
      if todo_index < 0 or todo_index > len(todo_list):
        print(Fore.RED + "the todo you are trying to delete is not in the list!")
      else:
        todo_to_delete = todo_list[todo_index]
        delete_confirmation = input(Fore.RED + f"Are you sure you want to delete '{todo_to_delete}'?(y/n): ")
        if delete_confirmation.lower() == "y":
          deleted_todo = todo_list.pop(todo_index)
          print(Fore.RED + f"Deleted '{deleted_todo}'")
        else:
          print(Fore.RED + "Operation cancelled!")

  
  elif user_input == 3:
    if len (todo_list) == 0:
      print(Fore.RED + "No todo's yet!")

    else:
      todo_index = int(input(Fore.GREEN + "Which todo would you like to edit?: ")) -1
      if todo_index < 0 or todo_index > len(todo_list):
        print(Fore.RED + "the todo you are trying to edit is not in the list!")
      else:
        todo_to_update= todo_list[todo_index]



      
