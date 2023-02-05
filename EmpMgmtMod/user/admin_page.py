import json
from user import employee_page
from util.config import config_dict

#file paths
employee_file_path = config_dict.get('file_paths').get('employee')
login_file_path = config_dict.get('file_paths').get('login')

#print statements
printer = config_dict.get("print-stmts")
generic_statements = printer.get("generic")

class Admin():

	def __init__(self, username):
		self.username = username

	def access_check(self, user_name):

		'''
		Security Function: checks access of user requesting to perform admin specific functions.
		'''

		with open(login_file_path , 'r', encoding="utf8") as login_db:
			login_data = json.load(login_db)
		for login in login_data:
			if user_name == login.get("username"):
				if login.get("access_type") == 0:
					print("You do not have admin access!!")
					return False
				elif login.get("access_type") == 1:
					return True


	def display_admin_menu(self):

		"""
		Displays options to Admin Users.
		Authenticates users before allowing them to perform any edits to db
		"""

		while True:

			index = 1
			statements = printer.get('admin-menu')
			print(str(generic_statements.get("welcome")).format("Admin"))

			for statement in statements:
				print(f"{index}. {statement}")
				index = index + 1
			print(f"{index}. {generic_statements.get('exit')}")
			choice = input(f"{generic_statements.get('choice')}")

			match choice:
				case "1":
					if self.access_check(self.username):
						self.display_all_emp_details()
					else:
						break
				case "2":
					if self.access_check(self.username):
						self.add_employee()
					else:
						break
				case "3":
					if self.access_check(self.username):
						self.remove_employee()
					else:
						break
				case "4":
					if self.access_check(self.username):
						self.change_access()
					else:
						break
				case "5":
					employee_caller = employee_page.Employee(self.username)
					employee_caller.employee_menu_display()
				case "6":
					print(generic_statements.get('thank_you_message'))
					break
				case _:
					print(str(generic_statements.get('incorrect_input')).format("choice"))


	def display_all_emp_details(self):

		with open(employee_file_path, 'r', encoding="utf8") as emp_db:
			emp_data = json.load(emp_db)
		emp_list = emp_data.get('employees')
		for employee in emp_list:
			employee_caller = employee_page.Employee(employee.get('username'))
			employee_caller.display_employee_details()

	def add_employee(self):

		statements = printer.get("employee_info")
		enter_message = generic_statements.get("input_func")
		print(str(generic_statements.get('input_func')).format("New Employee's Details"))
		emp_name = input(enter_message.format(statements.get("emp_name")))
		age = input(enter_message.format(statements.get("age")))
		emp_id = input(enter_message.format(statements.get("emp_id")))
		username = input(enter_message.format(statements.get("username")))
		role = input(enter_message.format(statements.get("role")))
		dept = input(enter_message.format(statements.get("dept")))
		salary = input(enter_message.format(statements.get("salary")))

		new_emp = {"emp_name" : emp_name, "username" : username, "emp_id" : emp_id, "age" : age, "role" : role, "dept" : dept, "salary" : salary}

		with open(employee_file_path, 'r+', encoding="utf8") as emp_db:
			emp_data = json.load(emp_db)
			emp_list = emp_data.get("employees")
			emp_list.append(new_emp)
			emp_db.seek(0)
			json.dump(emp_data, emp_db, indent=4)

		print(f"Employee {generic_statements.get('add')}")


	def remove_employee(self):

		'''
		Displays all employees in the roster and deletes the user whose Emp_id is entered by admin user.
		'''

		self.display_all_emp_details()
		while True:
			del_id = input(str(generic_statements.get('input_func')).format("ID of Employee to be deleted"))

			confirm = input(generic_statements.get('confirm'))
			if(confirm.lower()[0] == 'n'):
				return


			#delete employee record.
			new_emp_data = []

			with open(employee_file_path, 'r', encoding="utf8") as emp_db:
				emp_data = json.load(emp_db)

			curr_emp_list = emp_data.get('employees')
			found = False
			del_uname = ''

			for emp in curr_emp_list:
				if emp.get('emp_id' ).__eq__(del_id):
					found = True
					del_uname = emp.get('username')
				else:
					new_emp_data.append(emp)
			with open(employee_file_path, 'r', encoding="utf8") as emp_db:
				emp_data = json.load(emp_db)

			if not found:
				print(f"Employee {generic_statements.get('404')}")
			else:
				dict_new = {'employees' : new_emp_data}
				with open(employee_file_path, 'w', encoding="utf8") as emp_db:
					json.dump(dict_new, emp_db, indent = 4)
				print(f"Employee {generic_statements.get('delete')}")

			#delete login information
			with open(login_file_path, 'r', encoding="utf8") as login_db:
				curr_login_list = json.load(login_db)

			new_login_data = []

			for login in curr_login_list:
				if login.get('username').__eq__(del_uname):
					found = True
				else:
					new_login_data.append(login)

			with open(login_file_path, 'w', encoding="utf8") as login_db:
				json.dump(new_login_data, login_db, indent=4)

			print((f"Employee Login {generic_statements.get('delete')}"))
			break
			

	def change_access(self):

		'''
		Accepts username input from Admin user and changes access of user to admin.
		'''

		while True:
			update_id = input(generic_statements.get.format("Username of desired User"))
			confirm = input(generic_statements.get("confirm"))
			if confirm.lower()[0] == 'n':
				return
			updated_login_data = []

			with open(login_file_path, 'r', encoding="utf8") as login_db:
				login_data = json.load(login_db)

			curr_login_list = login_data
			found = False

			for emp in curr_login_list:
				if emp.get('username' ).__eq__(update_id):
					found = True
					emp['access_type'] = 1
				updated_login_data.append(emp)

			if not found:
				print(f"Employee {generic_statements.get('404')}")
			else:
				with open(login_file_path, 'w', encoding="utf8") as emp_db:
					json.dump(updated_login_data, emp_db, indent = 4)
				print(f"Employee {generic_statements.get('update')}")
				break