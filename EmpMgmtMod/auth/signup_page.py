import json
import getpass
import hashlib
from util.config import config_dict
import vaccine.vaccine_details as vc

#file paths

employee_file_path = config_dict.get('file_paths').get('employee')
login_file_path = config_dict.get('file_paths').get('login')

#obtaining printing statements
printer = config_dict.get("print-stmts")
generic_statements = printer.get("generic")


class Signup():

	def add_new_login(self):

		print(generic_statements.get("login_welcome"))
		#setting up password for user registered by admin
		uname = input(generic_statements.get("input_func").format('Username'))
		with open(employee_file_path, 'r', encoding="utf8") as emp_db:
			emp_file = json.load(emp_db)
		emp_data = emp_file.get('employees')
		username = []
		for emp in emp_data:
			username.append(emp.get('username'))
		if uname not in username:
			print(generic_statements.get("unregistered"))
			return

		#Hashing password to add security
		password = getpass.getpass(str(generic_statements.get("input_func")).format('Password'))
		hashed = hashlib.sha512(password.encode())
		final = hashed.hexdigest()
		
		#call Vaccine class
		vaccine_caller = vc.Vaccine()

		#Accept Vaccination Details from user
		print(str(generic_statements.get("input_func")).format('Vaccination Details'))
		vac_details = printer.get("vaccine_info")
		while True:
			vac_type = input(vac_details.get("vac_type"))
			if vaccine_caller.type_check(vac_type):
				break
			else:
				print(str(generic_statements.get("incorrect_input").format("Vaccination Type")))
		doses = int(input(vac_details.get("doses")))
		latest_date = input(vac_details.get("latest_date"))
		boast = input(vac_details.get("boaster"))
		if boast.lower()[0] == 'y':
			boaster = True
		else:
			boaster = False

		#save Vaccination details to file.
		vaccine_caller.add_vaccination_detail(uname, vac_type, doses, latest_date, boaster)

		#saving username password to file.
		new_user = {"username" : uname, "password" : final, "access_type" : 0}
		with open(login_file_path, 'r+', encoding="utf8") as login_db:
			login_data = json.load(login_db)
			login_data.append(new_user)
			login_db.seek(0)
			json.dump(login_data, login_db, indent = 4)

		print(f"{uname} {generic_statements.get('add')}")