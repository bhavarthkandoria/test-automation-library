from selenium import webdriver

class BrowserActions:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome()

    def open_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()
