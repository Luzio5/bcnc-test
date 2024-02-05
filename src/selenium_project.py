import os
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://bcncgroup.com/"

class Lang(Enum):
    en = ''
    es = 'es'
    de = 'de'
    fr = 'fr'

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, language: Lang):
        if language == Lang.en:
            self.driver.get(base_url)
        else:
            self.driver.get(f"{base_url}{language.value}")

    def get_paragraphs(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'page__content page__content--home js-page')]//p")

class WhoWeArePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, language: Lang):
        if language == Lang.en:
            self.driver.get(base_url + "who-we-are/")
        else:
            self.driver.get(f"{base_url}{language.value}/quienes-somos/" if language == Lang.es else
                            f"{base_url}{language.value}/vorstellung/" if language == Lang.de else
                            f"{base_url}{language.value}/a-propos-de-nous/")

    def get_paragraphs(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'page__content js-page')]//p")

def main():
    # Configuración del driver
    # opciones de navegador
    options = webdriver.ChromeOptions()
    #options.add_argument('--start-maximized')
    options.add_argument('--dissable-extensions')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')  # Ejecución sin interfaz gráfica

    # Get user's home directory
    home_dir = os.path.expanduser("~")
    # Path to ChromeDriver executable
    chromedriver_path = os.path.join(home_dir, "chromedriver")

    # Chrome service
    service = Service(executable_path=chromedriver_path)

    # Inicializa el navegador
    driver = webdriver.Chrome(service=service, options=options)
    for lang in Lang:
        # Load Home page
        home_page = HomePage(driver)
        home_page.load(lang)

        # Print paragraphs from Home page
        print(f"Language: {lang.name}")
        paragraphs = home_page.get_paragraphs()
        if paragraphs:
            for paragraph in paragraphs:
                if paragraph.text.strip():  # Check if paragraph text is not empty or whitespace only
                    print(paragraph.text)
                    print('--------------------------------------------')
        else:
            print("No paragraphs found on Home page")

        # Load Who We Are page
        who_we_are_page = WhoWeArePage(driver)
        who_we_are_page.load(lang)

        # Print paragraphs from Who We Are page
        print("WHO WE ARE:")
        paragraphs = who_we_are_page.get_paragraphs()
        if paragraphs:
            for paragraph in paragraphs:
                if paragraph.text.strip():  # Check if paragraph text is not empty or whitespace only
                    print(paragraph.text)
                    print('--------------------------------------------')
        else:
            print("No paragraphs found on Who We Are page")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
