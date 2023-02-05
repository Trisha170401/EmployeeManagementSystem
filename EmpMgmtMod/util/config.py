config_dict = {
    "file_paths" : {
        "login" : "auth/login.json",
        "employee" : "user/employee.json",
        "vaccine" : "vaccine/vaccine.json"
    },

    "print-stmts" : {
        "generic" : {
            "exit" : "Exit",
            "input_func" : "Enter {} : ",
            "thank_you_message" : "Thank you!!! Logging out.",
            "incorrect_input" : "Invalid {}, please try again",
            "unregistered" : "Sorry! Username not Registered. Please Contact the Admin.",
            "choice" : "Please Enter your choice: ",
            "welcome" : "Welcome {}. Select a Function",
            "login_welcome" : "Welcome to Employee Management System",
            "confirm" : "Are you sure? Yes or No: ",
            "add" : " records added Successfully",
            "update" : " records updated Successfully",
            "delete" : " records deleted Successfully",
            "404" : "records Not Found",
            "seperator" : "----------------------------------------------"
        },

        "login_menu" : [
            "Login",
            "Signup"
        ],

        "admin-menu" : [
            "Display All Employee Data",
            "Add New Employee",
            "Remove Employee",
            "Provide Admin Access",
            "Personal Information"
        ],

        "employee-menu" : [
            "Display Employee Details", 
            "Update Vaccination Details"
        ],

        "vaccination" :{ 
            "vac_type" : "Vaccine Type: ",
            "dose" : "Doses Taken: ",
            "latest_date" : "Date of Latest Vaccination: ",
            "boaster" : "Boaster Dose: "
        },

        "employee_info" : {
            "emp_name" : "Employee Name ", 
            "emp_id" : "Employee ID ",
            "username" : "Employee Username ", 
            "age" : "Age ", 
            "dept" : "Department ", 
            "role" : "Role ", 
            "salary" : "Salary "
        },

        "vaccine_info" : {
            "vac_type" : "Vaccine Type: ",
            "doses" : "Doses Taken: ",
            "latest_date" : "Date of Latest Vaccination (dd-mm-yyyy): ",
            "boaster" : "Have you taken the Boaster dose? yes or no: "
        }
    }
}