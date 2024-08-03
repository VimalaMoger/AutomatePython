import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://www.python.org')

button1 = driver.find_element('xpath', '/html/body')
button1.click()
time.sleep(10)
try:
    element = WebDriverWait(driver, 10).until(

        ec.presence_of_element_located(('xpath','//*[@id="id-search-field"]'))

    )
    
    element.click()
    element.clear()
    element.send_keys('dict')
    element.send_keys(Keys.RETURN)
    
    time.sleep(100)



   # ActionChains(driver).move_to_element(element).click(element).send_keys('kids').perform()

finally:
    driver.quit()


