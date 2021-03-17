from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://hk.finance.yahoo.com/quote/0175.HK/history?period1=1127952000&period2=1615939200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true")



screen_height = driver.execute_script("return window.screen.height;") 
i=1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 10
    time.sleep(0.1)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

table = driver.find_element_by_tag_name("table")
trlist = driver.find_elements_by_tag_name('tr')

for row in trlist: 
    tdlist = row.find_elements_by_tag_name('td')
    for col in tdlist:
        # print(col.text+ '\t', end='')
        print(col.text + '\t', end='')
    print('\n')
