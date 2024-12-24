from behave import then
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration import Config
    
@then('Verify exact text "{text}" is available')
def verify_text(context, text):
    xpath = f"//*[normalize-space(text())='{text}']"
    try:
        wait = WebDriverWait(context.driver, Config.EXPLICIT_WAIT) 
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(f'Step failed. Element with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

