from selenium.webdriver.common.by import By
class Form:
    edit_form = 'form'
    close_btn = '[data-testid="CloseIcon"]'

    def __init__(self, driver):
        self.driver = driver

    def check_form(self):
        form = self.driver.find_element(By.TAG_NAME, self.edit_form)
        if form.is_displayed():
            return True
        else:
            print('Форма не отображается')
            return False

    def close_form(self):
        self.driver.find_element(By.CSS_SELECTOR, self.close_btn).click()

    def fill_form(self, args):
        for [field, value] in args.items():
            selector = f'input[name="{field}"]'
            self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)