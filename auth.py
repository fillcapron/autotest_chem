from selenium.webdriver.common.by import By

class Auth:
    input_email = 'input[name="email"]'
    input_pasword = 'input[name="password"]'
    submit_button = 'button[type="submit"]'

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login, password):
        self.driver.find_element(By.CSS_SELECTOR, self.input_email).send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, self.input_pasword).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.submit_button).click()