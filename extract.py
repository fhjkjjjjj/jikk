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
 url = f"https://tgapp.herewallet.app/#{url}&tgWebAppVersion=7.0&tgWebAppPlatform=android&tgWebAppBotInline=1"
 chrome_options = webdriver.ChromeOptions()
 chrome_options.add_argument("--headless")
 chrome_options.add_argument("--no-sandbox")
 chrome_options.add_argument("--disable-dev-shm-usage")
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
 driver.execute_script("document.body.style.zoom='50%'")
# driver.get("https://tgapp.herewallet.app/#tgWebAppData=query_id%3DAAHR_k08AgAAANH-TTyil6SQ%26user%3D%257B%2522id%2522%253A5306711761%252C%2522first_name%2522%253A%2522Aman%2520%25F0%259F%2590%25AF%2522%252C%2522last_name%2522%253A%2522%257C%2520Finder_%25F0%259F%259A%2597%2522%252C%2522username%2522%253A%2522amanmondal444%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1710771926%26hash%3D154ea76c4263f1144ce67d2f8480e99affd11cdb504b227c2ea68fcdbc3211f5&tgWebAppVersion=7.0&tgWebAppPlatform=android&tgWebAppBotInline=1")
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
 # driver.get("https://tgapp.herewallet.app/hot")
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
