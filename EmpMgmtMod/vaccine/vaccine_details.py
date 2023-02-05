import json
from util.config import config_dict

#file paths:
vaccine_file_path = config_dict.get('file_paths').get('vaccine')

#print statements
printer = config_dict.get("print-stmts")
generic_statements = printer.get("generic")


class Vaccine():

	def type_check(self, vac_type):

		"""
		Checks whether vaccine type is registered in the country
		"""

		with open(vaccine_file_path, 'r', encoding="utf8") as vac_db:
			vac_data = json.load(vac_db)
		vac_list = vac_data.get('Vaccines')
		types = []
		for vaccine in vac_list:
			types.append(vaccine.get('vaccine_type'))
		return vac_type in types


	def add_vaccination_detail(self, username, vac_type, doses, latest_date, boaster):

		if self.type_check(vac_type):
			new_emp_data = {"username":username, "vaccine_type" : vac_type, "latest_date" : latest_date, "doses" : doses, "boaster" : boaster}
			with open(vaccine_file_path, 'r+', encoding="utf8") as vaccine_db:
				vaccine_data = json.load(vaccine_db)
				emp_data = vaccine_data.get('Employee_Vaccinations')
				emp_data.append(new_emp_data)
				vaccine_db.seek(0)
				json.dump(vaccine_data, vaccine_db, indent=4)
			print(f"Vaccination {generic_statements.get('add')}")
		else:
			print(str(generic_statements.get("incorrect_input")).format('Vaccination Type'))



	def update_dose(self, username, vac_type, doses, latest_date, boaster):

		if self.type_check(vac_type):
			updated_vac_detail = {"username": username, "vaccine_type": vac_type, "latest_date": latest_date, "doses": doses, "boaster": boaster}
			with open(vaccine_file_path, 'r+', encoding="utf8") as vaccine_db:
				vaccine_data = json.load(vaccine_db)
				emp_vac_data = vaccine_data.get('Employee_Vaccinations')
				updated_vac_list = []
				for emp_data in emp_vac_data:
					if emp_data.get('username') == username:
						updated_vac_list.append(updated_vac_detail)
					else:
						updated_vac_list.append(emp_data)
				vaccine_data["Employee_Vaccinations"] = updated_vac_list
				vaccine_db.seek(0)
				json.dump(vaccine_data, vaccine_db, indent=4)
			print(f"Vaccination {generic_statements.get('update')}")
			return True
		else:
			print(generic_statements.get("incorrect_input").format('Vaccination Type'))
			return False
		

	def display_vaccination_details(self, username):

		with open(vaccine_file_path, 'r', encoding="utf8") as vaccine_db:
			vaccine_data = json.load(vaccine_db)
		emp_data = vaccine_data.get('Employee_Vaccinations')
		found = False

		statements = printer.get('vaccination')

		for emp in emp_data:
			if(emp.get("username").__eq__(username)):
				print(generic_statements.get('seperator'))
				print("Latest Vaccination Details:")
				print(f"{statements.get('vac_type')}{emp.get('vaccine_type')}")
				print(f"{statements.get('dose')}{emp.get('doses')}")
				print(f"{statements.get('latest_date')}{emp.get('latest_date')}")
				print(f"{statements.get('boaster')}{emp.get('boaster')}")
				print(generic_statements.get('seperator'))
				found = True
				break
		if not found:
			print(f"User {generic_statements.get('404')}")