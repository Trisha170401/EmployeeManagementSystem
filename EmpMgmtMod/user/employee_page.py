from vaccine.vaccine_details import Vaccine
from util.config import config_dict
import json

#file paths
employee_file_path = config_dict.get('file_paths').get('employee')

#printing statements
printer = config_dict.get("print-stmts")
generic_statements = printer.get("generic")

class Employee():


	def __init__(self, emp_username):

		'''
		takes employee user name as parameter, reads data base to retrieve data from the database to fill in other class variables
		'''

		self.emp_username = emp_username


		#reading from employee database
		with open(employee_file_path, 'r', encoding="utf8") as employee_file:
			employee_info = employee_file.read()
		employee_db = json.loads(employee_info)
		employee_data = employee_db.get('employees')
		found = -1
		for emp in range(len(employee_data)):
			if(employee_data[emp].get("username").__eq__(emp_username)):
				found = emp
				break
		if found!=-1:
			self.emp_name = employee_data[emp].get('emp_name')
			self.emp_id = employee_data[emp].get('emp_id')
			self.age = employee_data[emp].get("age")
			self.salary = employee_data[emp].get("salary")
			self.role = employee_data[emp].get("role")
			self.dept = employee_data[emp].get("dept")
	
	def display_employee_details(self):

		statements = printer.get("employee_info")

		print(generic_statements.get("seperator"))
		print(f"{statements.get('emp_name')}: {self.emp_name}")
		print(f"{statements.get('emp_id')}: {self.emp_id}")
		print(f"{statements.get('username')}: {self.emp_username}")
		print(f"{statements.get('age')}: {self.age}")
		print(f"{statements.get('role')}: {self.role}")
		print(f"{statements.get('dept')}: {self.dept}")
		print(f"{statements.get('salary')}: {self.salary}")
		#call display class in Vaccine class
		vaccine_caller = Vaccine()
		vaccine_caller.display_vaccination_details(self.emp_username)
		print(generic_statements.get("seperator"))

	def update_vaccine_info(self):

		#call method of Vaccine class
		vaccine_caller = Vaccine() 
		#get input details from user
		vac_details = printer.get("vaccine_info")
		while True:
			vac_type = input(vac_details.get("vac_type"))
			if vaccine_caller.type_check(vac_type):
				break
			else:
				print(str(generic_statements.get("incorrect_input").format("Vaccination Type")))
		doses = int(input(vac_details.get("doses")))
		latest_date = input(vac_details.get("latest_date"))
		while True:
			boast = input(vac_details.get("boaster"))
			if(boast.lower()[0] == 'y'):
				boaster = True
				break
			elif(boast.lower()[0] == 'n'):
				boaster = False
				break
			else:
				print(str(generic_statements.get("incorrect_input")).format('Vaccination Details'))
		#update details
		vaccine_caller.update_dose(self.emp_username, vac_type, doses, latest_date, boaster)
		
	def employee_menu_display(self):

		while True:
			index = 1
			statements = printer.get('employee-menu')
			print(str(generic_statements.get("welcome")).format('Employee'))
			for statement in statements:
				print(f"{index}. {statement}")
				index = index + 1
			print(f"{index}. {generic_statements.get('exit')}")
			choice = int(input(generic_statements.get("choice")))

			match choice:
				case 1:
					self.display_employee_details()
				case 2:
					self.update_vaccine_info()
				case 3:
					print(generic_statements.get("thank_you_message"))
					break
				case _:
					print(str(generic_statements.get("incorrect_input")).format('choice'))