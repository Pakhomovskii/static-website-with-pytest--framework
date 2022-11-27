from page_objects.base_page import BasePage
from data.locators import HeaderLocators, FooterLocators


class MainPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://pakhomovskii.github.io/traveling-in-vietnam/"
        self.head_locators = HeaderLocators
        self.footer_locators = FooterLocators

        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)
    
    def check_title(self, title):
        assert self.get_title() == title

    def check_header_block(self):
        self.driver.find_element(*self.head_locators.SUBTITLE)
        self.driver.save_screenshot("results/results_header.png")

    def check_footer(self):
        self.driver.find_element(*self.footer_locators.FOOTER_MAPS).click()
        self.driver.find_element(*self.footer_locators.FOOTER_TRAVELLING).click()
        self.driver.find_element(*self.footer_locators.FOOTER_GITHUB).click()
        self.driver.find_element(*self.footer_locators.FOOTER_WEATHER).click()
        self.driver.find_element(*self.footer_locators.FOOTER_CALENDAR).click()
        self.driver.save_screenshot("results/results_footer.png")
