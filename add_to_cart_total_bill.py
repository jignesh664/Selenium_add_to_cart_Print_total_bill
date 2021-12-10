from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
import unittest
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()

driver.get("https://shop.one-shore.com/index.php")
driver.maximize_window()

#search sweater
driver.find_element(By.NAME, "s").click()
driver.find_element(By.NAME, "s").send_keys("HUMMINGBIRD PRINTED SWEATER")
driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)

#click on sweater
enter=By.XPATH,"/html/body/main/section/div/div/section/section/div[3]/div/div[1]/div/article/div/a/img"
enter_s=driver.find_element(*enter).click()
time.sleep(3)

# select size
size_select=By.XPATH,"/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/select"
size_select=driver.find_element(*size_select).send_keys("L")
time.sleep(3)

# select quantity
select_quantity=By.XPATH, "/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/input"
quantity=driver.find_element(*select_quantity)
quantity.send_keys(Keys.DELETE)
time.sleep(5)
quantity.send_keys("5")
time.sleep(3)

#add to card
add_to_card=By.XPATH,"/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[2]/button"
driver.find_element(*add_to_card).click()
time.sleep(3)

# checkout
process_checkout=By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/a"
driver.find_element(*process_checkout).click()
time.sleep(3)

#final checkout
final_checkout=By.CSS_SELECTOR,"#main > div > div.cart-grid-right.col-xs-12.col-lg-4 > div.card.cart-summary > div.checkout.cart-detailed-actions.card-block > div > a"
driver.find_element(*final_checkout).click()

#print total bill
subtotal_locator=By.XPATH,"/html/body/section/div/section/div/div[2]/section/div[1]/div[2]/div[1]/span[2]"
subtotal=driver.find_element(*subtotal_locator)

shipping_locator=By.XPATH,"/html/body/section/div/section/div/div[2]/section/div[1]/div[2]/div[2]/span[2]"
shipping=driver.find_element(*shipping_locator)

tax_locator=By.XPATH,"/html/body/section/div/section/div/div[2]/section/div[2]/div[3]/span[2]"
tax=driver.find_element(*tax_locator)

total_locator=By.XPATH,"/html/body/section/div/section/div/div[2]/section/div[2]/div[2]/span[2]"
total=driver.find_element(*total_locator)

print("Subtotal",subtotal.text)
print("Shppping",shipping.text)
print("Taxes",tax.text)
print("Total Bill",total.text)






