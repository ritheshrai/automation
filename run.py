import sys, clipboard, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secret import username, password

driver = webdriver.Chrome()
# Visiting https://github.com/login
driver.get("https://github.com/login")
# User login
driver.implicitly_wait(5)
username1 = driver.find_element_by_xpath('//*[@id="login_field"]')
username1.send_keys(username)
passwrd = driver.find_element_by_xpath('//*[@id="password"]')
passwrd.send_keys(password)
signin = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
signin.click()
print(signin)
# New repository creation
driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
# giving name t ur repsitry
driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(sys.argv[1])

# driver.find_element_by_xpath('//*[@id="repository_license_template_toggle"]').click()
# #adding Basic MIT licence
# waiter = WebDriverWait(driver, 10)
# select = waiter.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="details-3c0c67"]/summary')))
# select.click()
# licens = waiter.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filter-menu-738364"]/div/label[4]')))
# licens.click()

# checking for create button to let us click it
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="new_repository"]/div[4]/button')))
print(element)
element.click()
# copying the github repository link
driver.find_element_by_xpath(
    '//*[@id="js-repo-pjax-container"]/div[2]/div/git-clone-help/div[1]/div/div[4]/div/span/span/clipboard-copy').click()
# copied link to clipboard
cmd = clipboard.paste()
os.system('cmd /k gitwrk '+cmd+' '+sys.argv[1])
