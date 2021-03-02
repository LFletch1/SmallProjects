from selenium import webdriver

# base_url = 'https://www.wtamu.edu/about/information/covid-19/index.html'
base_url = 'https://login.wtamu.edu/cas/login?service=https%3A%2F%2Fmybuff.wtamu.edu%2F'
PATH = 'C:\Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
wt_page = driver.get(base_url)
# num = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[1]/div[3]/div/div/p[4]/strong/u[0]")
username_input = driver.find_element_by_id('username')
username_input.send_keys('********')

password = driver.find_element_by_id('password')
password.send_keys('*****************')
sign_in_button = driver.find_element_by_name('submit')
sign_in_button.click()

# driver.find_element_by_class_name('button')
# time.sleep(80)
# Cancel button xpath -->  //*[@id="messages-view"]/div/div[2]/div/button
passcode_button = driver.find_element_by_id('passcode')
passcode_button.click()
# chain = webdriver.common.action_chains.ActionChains(driver) Could be useful when creating gym scipt automation
input()
driver.quit()
