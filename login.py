import os


class User:
    def __init__(self, name=None, surname=None, login=None, password=None, age=None):
        """Classnin asosiy metodi"""
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.age = age
        self.number = ['1', '2', '3', '4']

    @staticmethod
    def show_print():
        """Ekranga chiqarish metodi"""
        print("""
        Welcome to the my Homepage
        
          Registration   >> 1 <<
          Login          >> 2 <<
        """)

    def selection(self):
        """Tanlash uchun metod"""
        self.clear()
        self.show_print()

        enter = input("Enter number [1/2]: ").strip()
        while enter not in self.number[:2]:
            self.clear()
            print("You enter an invalid number, Please try again")
            enter = input("Enter number [1/2]: ").strip()

        if enter == self.number[0]:
            self.registration()
        else:
            self.log_in()

    def registration(self):
        """Ro'yhatdan o'tish uchun metod"""
        self.clear()
        print("Registration process")

        new_name = input("Enter yor name: ").strip().capitalize()
        while not new_name:
            self.clear()
            print("You entered the wrong characters, Please try again")
            new_name = input("Enter yor name: ").strip().capitalize()

        new_surname = input("Enter your surname: ").strip().capitalize()
        while not new_surname:
            self.clear()
            print("You entered the wrong characters, Please try again")
            new_surname = input("Enter your surname: ").strip().capitalize()

        new_login = input("Enter your login: ").strip().lower()
        while not new_login:
            self.clear()
            print("You entered the wrong characters, Please try again")
            new_login = input("Enter your login: ").strip().lower()

        new_password = input("Enter your password: ").strip()
        while not new_password:
            self.clear()
            print("You entered the wrong characters, Please try again")
            new_password = input("Enter your password: ").strip()

        check_password = input("Enter check password: ")
        while not check_password:
            print("You entered the wrong characters, Please try again")
            check_password = input("Enter check password: ")

        new_age = input("Enter your age: ").strip()
        while not new_age:
            self.clear()
            print("You entered the wrong characters, Please try again")
            new_age = input("Enter your age: ").strip()

        print("Tabriklaymiz")

    def log_in(self):
        """Tizimga kirish uchun metod"""
        print("Tizimga kirdingiz")

    def log_out(self):
        """Tizimdan chiqish metodi"""
        pass

    def rename_account(self):
        """Accountni o'zgartirish metodi"""
        pass

    def delete_account(self):
        """Accountni o'chirish metodi"""
        pass

    @staticmethod
    def clear():
        """Tozalovchi metod"""
        os.system("clear")

user = User()
user.selection()
