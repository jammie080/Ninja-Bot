from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from package.Daily_Benefit import daily_benefit

from function.window import Window

class app:

	def __init__(self):
		self.window = Window()
		self.chrome_options = Options()
		self.chrome_options.add_argument('disable-infobars')

	def set_up(self):
		#self.driver = webdriver.Chrome(executable_path="browser\chromedriver.exe",chrome_options=self.chrome_options)
		#self.driver.get("http://ninja.joyfun.com")
		self.window.set_up(".*Unlimited Ninja - .*")

	def tear_down(self):
		self.driver.close()