from selenium import webdriver
import time
from selenium.webdriver import ActionChains

from auth import Auth
from table import Table
from form import Form

edit_form = 'form'
close_btn = '[data-testid="CloseIcon"]'

#Initial test
driver = webdriver.Chrome()
action = ActionChains(driver)
auth = Auth(driver)
form = Form(driver)
table = Table(driver)
driver.get('http://localhost:3000/')

time.sleep(1)

auth.authorization('test@ya.ru', '12345678')

time.sleep(1)

if table.check_table():
    #table.click_row(1)
    table.add_position()
else:
    driver.close()

time.sleep(5)

if form.check_form():
    form.fill_form(
        {
            "name": "Натрий",
            "regNumber": "CAS7664-30-1",
            "partionNumber": "19",
            "dateOfComingConsigment": "11-09-2022",
            "consigmentExpirationDate": "26-05-2022",
            "countInConsigment": "40",
            "volumeOneInConsigment": "11",
            "unit": "гр"
        }
    )
else:
    driver.close()

time.sleep(5)
# form = driver.find_element(By.TAG_NAME, edit_form)
#
# time.sleep(1)#ждем отображение кнопки закрытия
#
# if form.is_displayed():
#     print('Форма редактирования отображается')
# else:
#     print('Форма не отобразилась')
#     driver.close()
#
# print('Жмем на кнопку закрыть')
# btn_close = driver.find_element(By.CSS_SELECTOR, close_btn)
# btn_close.click()


#End tests
driver.close()