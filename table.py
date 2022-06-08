import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Table:
    data_grid = 'MuiDataGrid-virtualScrollerRenderZone'
    speed_dial_btn = '[data-testid="MoreHorizIcon"]'
    add_btn = '[data-testid="AddIcon"]'

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def check_table(self):
        table = self.driver.find_elements(By.CLASS_NAME, self.data_grid)

        if len(table):
            return True
        else:
            print('Таблица не отображается')
            return False

    def click_row(self, id):
        selector = f'div[data-id="{id}"]'
        if self.check_table():
            row = self.driver.find_element(By.CSS_SELECTOR, selector)
            if row.is_displayed():
                self.action.double_click(row).perform()
        else:
            print('Строка не найдена')
            self.driver.close()

    def add_position(self):
        btn = self.driver.find_element(By.CSS_SELECTOR, self.speed_dial_btn)
        if btn.is_displayed():
            btn.click()
            time.sleep(1)
            btn_add = self.driver.find_element(By.CSS_SELECTOR, self.add_btn)
            if btn_add.is_displayed:
                btn_add.click()