import colorama
from colorama import Fore, Style, Back
colorama.init()


# class Person:
#     name = ''
#     skin_color = ''
#     height = ''
#     weight = ''
#     age = 0


#     def talk(a):
#         print(Fore.RED + Style.BRIGHT +  'I am talking...')

#     def eat(a):
#         print(Fore.RED + Style.BRIGHT + 'I am eating...')


#     def think(a):
#         print(Fore.RED + Style.BRIGHT + 'I am thinking...')
    







# male = Person()
# male.name = 'Derrick'
# male.talk()
# print(male.name)



# female = Person()

class User():
    first_name = ''
    last_name = ''
    username = ''
    password = ''
    dob = ''
    gender = ''

    def __init__(self, first_name, last_name, username, password, dob, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.dob = dob
        self.gender = gender

    def display_user(self):
        print(Fore.GREEN + self.first_name, self.last_name, self.username, self.password, self.dob, self.gender)


user = User('Derrick', 'Smith', 'DerrickSmith', '123456', '1990-01-01', 'Male')
user.display_user()

