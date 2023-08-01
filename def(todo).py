import colorama
from colorama import Fore, Back, Style

colorama.init()


#create a simple program that allows users to create a todo list

todo_list = []
user_input = 0


#main program loop
def main():
      user_input = int(input(Fore.BLUE + """ What would you like to do?
            1. Create a new todo
            2. Delete a todo
            3. Edit a todo
            4. List all todos
            5. Exit\n\n
            Select option: """))
      return user_input
  
def user_options(user_input):
    if user_input == 1:
        add_todo()
    elif user_input == 2:
        delete_todo()
    elif user_input == 3:
        edit_todo()
    elif user_input == 4:
        list_todo()
    elif user_input == 5:
        exit_todo()
    else:
        print(Fore.RED + "Invalid option!")
    
    user_input = main()
    user_options(user_input)
#Define user input function


    

def add_todo():
        user_input = input(Fore.BLUE + "Enter todo item: ")
        if user_input in todo_list:
            print(Fore.RED + "Todo already exists!")
        else:
            todo_list.append(user_input)
            print(Fore.GREEN + "Todo added successfully!")
# add_todo()
            
            
def delete_todo():
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
# delete_todo()
          
          
def edit_todo():
     if len (todo_list) == 0:
      print(Fore.RED + "No todo's yet!")

     else:
      todo_index = int(input(Fore.GREEN + "Which todo would you like to edit?: ")) -1
      if todo_index < 0 or todo_index > len(todo_list):
        print(Fore.RED + "the todo you are trying to edit is not in the list!")
      else:
        todo_update = input(Fore.GREEN + "Enter your todo update: ")
        todo_list[todo_index] = todo_update
        print(Fore.GREEN + "Todo updated successfully!")
# edit_todo()

def list_todo():
     if len (todo_list) == 0:
      print(Fore.RED + "No todo's yet!")
    
     else:
       print(Fore.GREEN + "Todo List:")
       for i, todo in enumerate(todo_list,start=1):
         print(Fore.YELLOW + f" {i}. {todo}")
         
# list_todo()

def exit_todo():
    print(Fore.RED + "Exiting program...")
    exit(0)
    
    
    
user_input = main()
user_options(user_input)
            

    
    