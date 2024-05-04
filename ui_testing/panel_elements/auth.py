import time
from selenium.webdriver.common.by import By
from ui_testing.base_page import BasePage
from allure import step
from ui_testing.panel_elements.panel_menu import MenuElement


class AuthPage(BasePage):
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log In')]")
    ACCOUNT_ICON = (By.CLASS_NAME, "account-icon")

    @step("Login in the control panel")
    def login(self, username, password):
        self.input_value(self.EMAIL_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.SIGN_IN_BUTTON)
        time.sleep(5)
        return MenuElement(self.browser)
