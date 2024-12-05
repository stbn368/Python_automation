from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from configuration import Config
import chromedriver_autoinstaller

def before_all(context):
    # Install automatically Chromedriver
    chromedriver_autoinstaller.install()
    
    # Set up driver
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(Config.IMPLICIT_WAIT)
    context.driver.maximize_window()

def before_scenario(context, scenario):
    """
    Navigate to the home page for each scenario
    """
    context.driver.get(Config.BASE_URL)

def after_all(context):
    # Close driver
    context.driver.quit()
