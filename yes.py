from autotest_lib.client.common_lib.cros import chromedriver
with chromedriver.chromedriver() as chromedriver_instance:
   driver = chromedriver_instance.driver

URL = "www.instagram.com"

driver.get(URL)
