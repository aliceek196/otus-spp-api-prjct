from selenium.webdriver.common.by import By
from ui_testing.base_page import BasePage
from allure import step
from ui_testing.vstack_servers.vstack_servers_calc import VstackServersCalculatorPage


class VstackServersListPage(BasePage):
    CREATE_SERVER_BUTTON = (By.XPATH, "//*[text()='Создать сервер']")

    @step("Click create server button in servers landing page")
    def click_create_vstack_server(self):
        self.click(self.CREATE_SERVER_BUTTON)
        return VstackServersCalculatorPage(self.browser)