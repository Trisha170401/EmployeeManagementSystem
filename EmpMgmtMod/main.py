"""
calls login_module to start running the Employee Management System.
"""

from auth.login_page import Login
if __name__ == '__main__':
    runner_obj = Login()
    runner_obj.login_menu_display()

