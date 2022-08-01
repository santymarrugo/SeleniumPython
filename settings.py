valor = "12"
'''
# Ejecutar los test con selenium y Python en modo Headless con Chrome

options = webdriver.ChromeOptions()
options.headless = True
self.driver = webdriver.Chrome(options=options, service=Service("../chromedriver.exe"))
self.driver.get("https://memorycontywebtesting.azurewebsites.net")

# Ejecutar los test con selenium y Python en modo Headless con Firefox

options = webdriver.FirefoxOptions()
options.headless = True
self.driver = webdriver.Firefox(options=options, service=Service("../geckodriver.exe"))
self.driver.get("https://memorycontywebtesting.azurewebsites.net")

# Ejecuta los test con selenium y Python en modo Incognito en Firefox
 
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
self.driver = webdriver.Firefox(firefox_profile, service=Service("../geckodriver.exe"))
self.driver.get("https://memorycontywebtesting.azurewebsites.net")

# Ejecuta los test con selenium y Python en modo Incognito en Chrome

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
self.driver = webdriver.Chrome(chrome_options, service=Service("../chromedriver.exe"))
self.driver.get("https://memorycontywebtesting.azurewebsites.net")
'''