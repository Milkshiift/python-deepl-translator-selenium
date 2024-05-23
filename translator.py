from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions() 

options.add_argument('--headless') # Remove this to see the browser window
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# These are maybe useless, but hopefully not
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-extensions')
options.add_argument('--disable-background-networking')
options.add_argument('--disable-default-apps')
options.add_argument('--disable-sync')
options.add_argument('--disable-translate')
options.add_argument('--metrics-recording-only')
options.add_argument('--no-first-run')
  
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options) 
url = f"https://www.deepl.com/translator#en/uk/"
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-labelledby='translation-source-heading']")))
# Precaching input and output elements
input_element = driver.find_element(By.XPATH, "//div[@aria-labelledby='translation-source-heading']")
target_element = driver.find_element(By.XPATH, "//div[@aria-labelledby='translation-target-heading']")

async def get_translation(text, langFrom, langTo):
    url = f"https://www.deepl.com/translator#{langFrom}/{langTo}/"
    driver.get(url)

    # ⚠️ Action chains are not instantanious
    ActionChains(driver).send_keys_to_element(input_element, text).perform()

    # When the Undo button appears, translation is finished
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='empty:hidden']//span[@data-testid='deepl-ui-tooltip-container']")))

    translation = target_element.text
        
    return translation