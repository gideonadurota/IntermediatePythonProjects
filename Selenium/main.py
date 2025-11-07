import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    # Old way of doing it. You had to download and pass the driver
    # def __init__(self, driver: str):
    #     self.service = Service(driver)
    #     self.browser = webdriver.Chrome(service=self.service
    def __init__(self):
        self.browser = webdriver.Chrome()

    def open_page(self, url: str):
        print(f'Opening {url}')
        self.browser.get(url)

    def close_browser(self):
        print('Closing browser')
        self.browser.close()

if __name__ == '__main__':
    # browser = Browser("C:\\Windows\\chromedriver.exe")  -- Old way
    browser = Browser()

    browser.open_page('https://www.python.org')
    time.sleep(5)