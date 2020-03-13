import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['enableVNC'] = True
capabilities['enableVideo'] = True
capabilities['videoName'] = 'my-video-c1.mp4'
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities)
driver.get('https://google.com')
element = driver.find_element_by_name('q')
element.send_keys('生産性向上ブログ')
element.submit()
driver.quit()
