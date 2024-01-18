import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


#url = 'https://www.ragasurabhi.com/carnatic-music/songs.html'
url='https://edube.org/login'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get(url)
    #file_element = driver.find_element(By.XPATH, '//p[@class="body_indexpage_para"]/a[@class="body_indexpage_assetlinktext"]')
    file_element = driver.find_element(By.XPATH,
                                       '//a[@class="signup" and @href="/registration"]')
    time.sleep(5)
    file_element.click()
    time.sleep(5)

finally:
    driver.quit()
