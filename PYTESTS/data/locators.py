from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO = (By.XPATH, "//img[@alt='Logo']")
    LANGUAGE_ = (By.CLASS_NAME, "header__lang-link']")
    SUBTITLE = (By.CLASS_NAME, "lead__subtitle")
    MAIN_PIC = (By.CLASS_NAME, "lead__image")
    TEXT_UNDER_MAIN_PIC = (By.CLASS_NAME, "lead__image")


class ContentLocators:
    pass


class FooterLocators:
    FOOTER_MAPS = (By.XPATH, "//a[@href='https://www.google.com/maps']")
    FOOTER_WEATHER = (By.XPATH, "//a[@href='https://weather.coms']")
    FOOTER_CALENDAR = (By.XPATH, "//a[@href='https://calendar.google.com']")
    FOOTER_TRAVELLING= (By.XPATH, "//a[@href='https://www.google.com/travel']")
    FOOTER_GITHUB = (By.XPATH, "//a[@href='https://github.com/Pakhomovskii/traveling-in-vietnam']")
