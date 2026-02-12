from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    BLOCK_WITH_EMAIL = (By.XPATH, "//strong[text()='Email:']/parent::p")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#errorMsg")
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, '#emailerror')
    LOGO = (By.CSS_SELECTOR, "a[class='text-decoration-none'] img[class='img-fluid']")
