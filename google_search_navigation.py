#file1
#open google.com
#search campusx
#learnwith.campusx.in
#dsmp course info

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# This keeps the window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# --- CAPTCHA BYPASS SETTINGS ---
# This hides the "Automation" flag from Google
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
# -------------------------------

s = Service(r"C:\Users\rudra\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Pass the options to the driver
driver = webdriver.Chrome(service=s, options=chrome_options)

# Extra script to make the browser look like a normal user
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

driver.get("https://www.google.com")
time.sleep(1)

#fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH,value = '//*[@id="APjFqb"]')
user_input.send_keys('Campusx')
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(2) # Increased slightly to let Google load without looking like a bot


link = driver.find_element(By.PARTIAL_LINK_TEXT, "CampusX")
link.click()


time.sleep(1)

link2 = driver.find_element(by=By.XPATH, value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()
