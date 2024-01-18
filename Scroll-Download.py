import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://catalog.data.gov/dataset?q=&sort=views_recent+desc'
download_folder = r'C:\Users\SRILEKHA\Downloads\Auto'  # Replace with the desired folder path

chrome_options = Options()
prefs = {'download.default_directory': download_folder}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get(url)

    # Wait for the elements to be present
    file_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//a[@class="label label-default" and @data-format="csv"]'))
    )[:2]

    for file_element in file_elements:
        file_url = file_element.get_attribute('href')
        file_name = os.path.join(download_folder, os.path.basename(file_url.split('?')[0]))

        # Use requests to download the file
        response = requests.get(file_url, stream=True)
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        time.sleep(1)  # You can adjust the sleep duration if needed

except KeyboardInterrupt:
    print("Script interrupted by user.")
finally:
    driver.quit()
