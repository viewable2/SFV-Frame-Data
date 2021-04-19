from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time #used for sleep
import os #log out to file
import io #back support
 
def get_profile():
    profile = webdriver.FirefoxProfile();
    profile.set_preference("browser.privatebrowsing.autostart", True)
    profile.update_preferences()
    return profile

def get_options():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    return options

def write_out(file):
    if os.path.exists("Scapper.log"):
        os.remove("Scapper.log")
    
    fwrite = io.open("Scapper.log", "x", encoding="utf-8")
    fwrite.write(file)
    fwrite.close()

def listToString(list):
    str1 = " "
    return (str1.join(list))

def main():
    path = 'geckodriver.exe'
    url = 'https://fullmeter.com/fatonline/#/framedata/SFV/Juri'

    driver = webdriver.Firefox(executable_path=path, firefox_profile=get_profile(), options=get_options() )
    driver.get(url)
    time.sleep(2)

    def clear(): os.system('cls') #on Windows System
    clear()

    try:
        data = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataTable"))
        )

        base = driver.find_elements_by_class_name("stat-chooser")

        tabs = ["test"]
        for tab in base:
            tabs.append(tab.text)
        tabs.pop(0)

        
        stats = driver.find_element_by_class_name("stat-row")
        statEntry = stats.find_elements_by_class_name("stat-entry")

        for statTree in tabs:
            base.__setattr__("value", statTree)
            



        #data = driver.find_elements_by_id(id_="video-title")

        write_out(strn) #log outfile








    finally:
        time.sleep(5)
        driver.quit()



main()