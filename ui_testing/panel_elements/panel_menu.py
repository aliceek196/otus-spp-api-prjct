from selenium.webdriver.common.by import By
from ui_testing.base_page import BasePage
from ui_testing.vstack_servers.vstack_servers_list import VstackServersListPage
from allure import step


class MenuElement(BasePage):
    VSTACK_CLOUD_FEATURE = (By.XPATH, "//*[text()='vStack Cloud']")
    VSTACK_CLOUD_SERVERS = (By.XPATH, "//a[contains(@href, '/vstack/servers/list')]/descendant::span[contains(text(), "
                                      "'Серверы')]")

    @step("Selecting vStack servers in the main menu of the control panel")
    def click_vstack_servers(self):
        self.get_element(self.VSTACK_CLOUD_SERVERS).click()
        return VstackServersListPage(self.browser)

