from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from allure import step


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    @step("Finding an element")
    def get_element(self, locator: tuple, timeout=7):
        return WebDriverWait(self.browser, timeout) \
            .until(EC.visibility_of_element_located(locator))

    @step("Move to element and click")
    def click(self, locator: tuple):
        ActionChains(self.browser) \
            .move_to_element(self.get_element(locator)) \
            .pause(0.3).click().perform()

    @step("Input string")
    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        for line in text:
            self.get_element(locator).send_keys(line)

    @step("Move an element to the viewable area of the screen")
    def scroll_into_view(self, locator):
        self.browser.execute_script("arguments[0].click();", locator)

    @step("Move an element to the viewable area of the screen and find it")
    def scroll_and_get_element(self, locator: tuple, timeout=7):
        element = WebDriverWait(self.browser, timeout) \
            .until(EC.visibility_of_element_located(locator))
        self.scroll_into_view(element)
        return element

    @step("Waiting for element disappeared")
    def element_disappeared(self, locator: tuple, timeout=240):
        return WebDriverWait(self.browser, timeout) \
            .until(EC.invisibility_of_element(locator))

    @step("Repeat click action")
    def repeat_action(self, locator, repetitions):
        for i in range(repetitions):
            self.get_element(locator).click()

    @step("Pressing the Enter key from the keyboard")
    def click_enter(self, locator):
        click_enter = WebDriverWait(self.browser, 3) \
            .until(EC.visibility_of_element_located(locator))
        click_enter.send_keys(Keys.ENTER)
