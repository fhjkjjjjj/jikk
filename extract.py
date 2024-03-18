from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
def get_reward(url,wallet):
 chrome_options = webdriver.ChromeOptions()
 chrome_options.add_argument("--headless")
 chrome_options.add_argument("--no-sandbox")
 chrome_options.add_argument("--disable-dev-shm-usage")
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
 print("\033[0;31mTrying To login account")
 driver.execute_script("document.body.style.zoom='50%'")
 driver.get(url)
 element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/button"))).click()
 element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/label/textarea"))).send_keys(wallet)
 element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/button"))).click()
 element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/button"))).click()
 user_name = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/p"))).text
 time.sleep(2)
 bal = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[1]/div[2]/div/p"))).text
 point = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/div[2]/div/p[2]"))).text
 mininged = False
 if float(point) > float(0.009):
  mininged = True
  element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/div[2]/div[1]/p"))).click()
  element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[2]/button"))).click()
  element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[2]/button"))).click()
  for i in range(99):
   check = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/h1"))).text
   check_gas = driver.page_source
   if "More Gas needed" in check_gas:
#    print("More Gas needed")
#    print("Paying 30% hot coin as a gass fee")
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div[2]/button"))).click()
   if float(check) != float(check):
    time.sleep(2)
    break
 else:
   print(f"\033[0;31mMIN COIN NEED 0.01 TO CLAIM")
 driver.delete_all_cookies()
 driver.execute_script("window.localStorage.clear();")
 driver.execute_script("window.sessionStorage.clear();")
# print("_" * 40)
 j = {
  "username":user_name, 
  "bal":bal, 
  "total_mining":point, 
  "mininged":mininged
 }
 return j



def download():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://google.com")
    title = driver.title
#    driver.close()
    return f"hello -> {title}"
def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
