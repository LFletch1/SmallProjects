# Lance Fletcher
# Web scraping program that grabs the value of weekly covid-19 WTAMU cases
# from the website and plots the values into a bar graph.
# 2/26/2021

from selenium import webdriver
from matplotlib import pyplot as plt

base_url = 'https://www.wtamu.edu/about/information/covid-19/index.html'
PATH = 'C:\Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
wt_page = driver.get(base_url)

covid_cases = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[4]/div/div/p[5]/strong/u[1]').get_attribute('innerHTML')
week = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[4]/div/div/p[5]/strong/u[2]').get_attribute('innerHTML')
week = week[:11] + '-' + week[12:]
week = week[:6] + week[8:19] + week[21:]
week = week.replace(' ', '')

append_file = open('weekly-cases.csv', 'a+')
append_file.write(week + ',' + covid_cases + '\n')  # write
append_file.seek(0,0)  # set read/write pointer to beginning of file

dates = []
cases = []
for line in append_file:
    elements = line.split(',')
    dates.append(elements[0])
    cases.append(int(elements[1]))

append_file.close()
print(dates)
print(cases)
driver.quit()

plt.bar(dates, cases)
plt.xticks(rotation=45)
plt.xlabel("Week")
plt.ylabel("COVID-19 Cases")
plt.show()
