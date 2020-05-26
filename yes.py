with chromedriver.chromedriver() as chromedriver_instance:
   driver = chromedriver_instance.driver

URL = "www.instagram.com"

driver.get(URL)
