import json
import getpass
import hashlib
from util.config import config_dict
from user import admin_page
from user import employee_page
import auth.signup_page as su

#setting file paths
login_file_path = config_dict.get('file_paths').get('login')

#obtaining printing statements
printer = config_dict.get("print-stmts")
generic_statements = printer.get("generic")

class Login():

    """
    adds login functionality
    """

    def validate_user(self, user_name, password):

        """
        checks access type of user
        """

        with open(login_file_path, 'r', encoding="utf8") as login:
            login_file = login.read()

        login_data = json.loads(login_file)
        access = False
        access_type = ''

        hashed = hashlib.sha512(password.encode())

        for user in login_data:
            if (user.get('username').__eq__(user_name) and user.get("password").__eq__(hashed.hexdigest())):
                access = True
                access_type = user.get("access_type")
                break

        return (access, access_type)

    def login_menu_display(self):

        """
        displays available options to users.
        """

        while True:
            print(generic_statements.get("login_welcome"))
            index = 1
            statements = printer.get("login_menu")
            for statement in statements:
                print(f"{index}. {statement}")
                index = index + 1
            print(f"{index}. {generic_statements.get('exit')}")
            choice = int(input(generic_statements.get('choice')))

            match choice:
                case 1:
                    while True:
                        user_name = input(generic_statements.get("input_func").format('Username'))
                        password = getpass.getpass(generic_statements.get("input_func").format('Password'))

                        (access, access_type) = self.validate_user(
                            user_name, password)
                        if access:
                            print("User Authenticated")
                            if access_type == 0:
                                # call employee menu display function
                                employee_caller = employee_page.Employee(
                                    user_name)
                                employee_caller.employee_menu_display()

                            elif access_type == 1:
                                # call admin menu display function
                                admin_caller = admin_page.Admin(user_name)
                                admin_caller.display_admin_menu()
                            break
                        else:
                            print(f"Username or Password {generic_statements.get('404')}")

                case 2:
                    signup_caller = su.Signup()
                    signup_caller.add_new_login()
                case 3:
                    print(generic_statements.get('thank_you_message'))
                    break
                case _:
                    print(str(generic_statements.get('incorrect_input')).format("choice"))