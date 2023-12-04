from abc import ABC, abstractclassmethod
from datetime import datetime
import re
import calendar
import json

class Shape(ABC):
  file_path = 'users_birthday.txt'
  file_path_phone = 'users_phone.txt'
    
  def __init__(self) -> None:
        super().__init__()

  @abstractclassmethod
  def draw(self):
        pass 

  @abstractclassmethod
  def area(self):
        pass 

  @abstractclassmethod
  def perimetr(self):
        pass 

class sustem(Shape):
   
  file_path = 'users_birthday.txt'
  file_path_phone = 'users_phone.txt'
    
  def add_user():
    
    file_path = 'users_birthday.txt'
    name = input('Plase enter name & birthday in this form "Name: birthday": ')
    with open(file_path, 'a') as file:
        file.write(name + '\n')
    print('Over super !')

  def delete_user():
    file_path = 'users_birthday.txt'
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        str = input('Plase enter Name contact: ')
        with open(file_path, 'w') as file:
            for line in lines:
                if not line.startswith(str):
                    file.write(line)
        print('Over, person was removed !')
    except FileNotFoundError:
        print('Oops, an error occurred !')

  def list_users():
    file_path = 'users_birthday.txt'
    
    with open(file_path, 'r') as file:
        come = file.read()
        print('')
        print('Your lis: ')
        print('')
        print(come)

  def add_phone():
    file_path_phone = 'users_phone.txt'

    name = input('Plase enter name & phone in this form "Name: +1XXXXXXXXX" (and email: Email.com): ')
    with open(file_path_phone, 'a') as file:
        file.write(name + '\n')
    print('Over, cntact has been added !')

  def delete_contect():
    file_path_phone = 'users_phone.txt'
    try: 
        with open(file_path_phone, 'r') as file:
            lines = file.readlines()
        str = input('Plase enter Name contact: ')
        with open(file_path_phone, 'w') as file: 
            for line in lines:
                if not line.startswith(str):
                    file.write(line)
        print('Over, contact was removed !')
    except FileNotFoundError:
        print('Oops,s an error occurred !')

  def list_contact():
    file_path_phone = 'users_phone.txt'
    with open(file_path_phone, 'r') as file:
        come2 = file.readlines() 
        come2.sort(key=lambda x: x.split(':')[0])

        current_letter = None
        print('')
        print('Pase this is your list')
        print('')
        for come in come2:
            name = come.split(':')[0]
            first_letter = name[0].upper()
            if first_letter != current_letter:
                print('_' * 25)  
                current_letter = first_letter
            print(come.strip()) 

  def saerch():
    file_path_phone = 'users_phone.txt'
    saer = input('Plase enter the username you went to search: ')
    found = False 
    with open(file_path_phone, 'r') as file:
        for line in file:
            name, phone = line.strip().split(':') 
            if saer == name:
                print(f'Username is {saer}: {phone}') #Выводит только перво найднеый контакт(нельзя вписывать два контакта одновремено)
                found = True 
                break
    if not found:
        print(f"Username '{saer}' not found in the file ")

  def change():
    file_path_phone = 'users_phone.txt'

    old_contact = input('Plase enter old contect: ')
    new_contact = input('Please enter the new information in full (it will be displayed for you exactly as you write it down): ')

    with open(file_path_phone, 'r') as file:
        lines = file.readlines()

    save_contect = []

    for line in lines:
        if old_contact in line:    # В контакте будет удалён всё, и все будет заменено на изменение 
            save_contect.append(new_contact + '\n')
        else:
            save_contect.append(line)

    with open(file_path_phone, 'w') as file:
        file.writelines(save_contect) 
    
    print('Over your contact change !')

  def birthday_chang():
    file_path = 'users_birthday.txt'

    old_birthday = input('Plase enter old birthday: ')
    new_birthday = input('Plase enter new birthday(plas name birthday people): ')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    save_birthday = []

    for line in lines:
        if old_birthday in line:
            save_birthday.append(new_birthday + '\n')
        else:
            save_birthday.append(line)

    with open(file_path, 'w') as file:
        file.writelines(save_birthday)

    print('Over, birthday has been changed')

  def calend():
    year = int(input('Please enter the year (2023): '))
    month = int(input('Please enter month (6): '))
    print(calendar.month(year, month))  

  def serch_user_birth():
    file_path = 'users_birthday.txt'
    strr = input('Plase enter the name of the btrthday person: ')
    found = False
    today = datetime.today()
    with open(file_path, 'r')as file:
        for line in file:
            name, birthday = line.strip().split(':') #strip
            if strr == name:
                print(f'User is {strr}: {birthday} ')
                found = True
                break
    if not found:
        print('User was not found in the file ')

  def serch_user_birth_date():
    file_path = 'users_birthday.txt'
    name_to_find = input('Please enter the name of the person whose birthday you are looking for: ')
    found = False
    today = datetime.today()
    with open(file_path, 'r') as file:
        for line in file:
            name, birthday_str = line.strip().split(':')
            if name_to_find == name:
                birthday_str = birthday_str.strip()  # Удалить начальные и конечные пробелы
                birthday = datetime.strptime(birthday_str, '%d.%m.%Y')
                next_birthday = birthday.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)
                days_until_birthday = (next_birthday - today).days
                print(f"Until the user's next birthday{name_to_find} left {days_until_birthday} days ")
                found = True
                break
    if not found:
        print('User not found in file ')

  def add_contact():
    file_path = 'users_birthday.txt'
    file_path_phone = 'users_phone.txt'
    name = input('Enter contact name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email address: ')
    address = input('Enter address: ')
    birthday = input('Enter birthday: ')

    with open(file_path_phone, 'a') as file:
        file.write(f"{name}: {phone} | {email} | {address} | {birthday}\n")

    print('Contact added successfully!')

  def display_contacts():
    file_path_phone = 'users_phone.txt'
    with open(file_path_phone, 'r') as file:
        contacts = file.readlines()

    for i, contact in enumerate(contacts, start=1):
        print(f'Contact{i}: {contact.strip()}')

  def delete_contact():
    file_path_phone = 'users_phone.txt'
    try:
        with open(file_path_phone, 'r') as file:
            lines = file.readlines()

        contact_to_delete = input('Enter the name of the contact to delete: ')

        with open(file_path_phone, 'w') as file:
            for line in lines:
                if not line.startswith(contact_to_delete):
                    file.write(line)

        print('Contact deleted successfully!')
    except FileNotFoundError:
        print('Oops, an error occurred!')

  while True:
        print('')
        print('What do you want to do ?')
        print('')
        print("Sorry, you can't add two identical names ")
        print('')
        print('1 - If you add a birthday person ')
        print('2 - Delete birthday a person ')
        print('3 - If you look at the list of birthdays ')
        print('4 - If you add a contact ')
        print('5 - Delete contact (by name) ')
        print('6 - Do you want to see the phone book ')
        print('7 - Edit information about Birthdays ') # 7 & 8 Можно находть и просто по имени 
        print('8 - Change the contact (please note that the contact will match your changes). We are not responsible for any loss of information ')
        print('9 - Search for user contacts ')
        # print('10 - Enter email user ')
        print('11 - Calendar) ') #Find out the next birthday of a contact (by name)
        print('12 - Find a birthday person by name ')
        print('13 - How many days left until next birthday by name ')
        print('14 - Добавить')
        print('15- Вывод')
        print('16- Удалить')
        print('17- Exit ')

        choice = input('Choose an action: 1, 2, 3 etc.. ? ')
        
        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            list_users()
        elif choice == '4':
            add_phone()
        elif choice == '5':
            delete_contect()
        elif choice == '6':
            list_contact()
        elif choice == '7':
            birthday_chang() 
        elif choice == '8':
            change()
        elif choice == '9':
            saerch()
        # elif choice == '10':
           # email()
        elif choice == '11':
           calend() #birthday_cont()
        elif choice == '12':
            serch_user_birth()
        elif choice == '13':
            serch_user_birth_date()
        elif choice == '14':
            add_contact()
        elif choice == '15':
            display_contacts()
        elif choice == '16':
            delete_contact()
        elif choice  == '17': 
            print('Over :)')
            break
        else:
            print('Oops, an error occurred !')

if __name__ == '__main__':
    qww =  sustem()