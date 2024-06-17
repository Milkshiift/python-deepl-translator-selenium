from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
url = "https://www.deepl.com/translator"
driver.get(url)

def get_translation(text, langFrom, langTo):
    driver.get(f"https://www.deepl.com/translator#{langFrom}/{langTo}/")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-labelledby='translation-source-heading']")))
    input_element = driver.find_element(By.XPATH, "//div[@aria-labelledby='translation-source-heading']")
    input_element.send_keys(text)

    target_element = driver.find_element(By.XPATH, "//div[@aria-labelledby='translation-target-heading']")

    # When the Undo button appears, translation is finished
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='empty:hidden']//span[@data-testid='deepl-ui-tooltip-container']")))

    translation = target_element.text

    return translation

print(get_translation("but daddy 🥺 👉 👈", "ru", "en"))

# Close the browser window
driver.quit()