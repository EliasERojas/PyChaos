from selenium import webdriver
from selenium.webdriver.common.by import By

driver : webdriver.Firefox = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")
title : str = driver.title
driver.implicitly_wait(3)
nana_chat = driver.find_element(By.XPATH,"//span[text()='Nana']")
nana_chat.click()
driver.implicitly_wait(0.5)

rows = driver.find_elements(By.XPATH, "//div[@role='row']")
rows_len = len(rows)
last_messages = rows[slice(rows_len-5,rows_len)]

for message in last_messages : 
    elem = message.find_element(By.XPATH, "//span[@class='selectable-text copyable-text']")
    if elem :
        print(elem.text)
    else :
        print("Audio")

driver.quit()
