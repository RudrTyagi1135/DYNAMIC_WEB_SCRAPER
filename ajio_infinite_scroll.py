#file2
#infinite scrolling

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


driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
time.sleep(2)

counter = 1
while True:


    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height



html = driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)