from behave import then
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.configuration import Config
    
@then('Verify exact text "{text}" is available')
def verify_text(context, text):
    xpath = f"//*[normalize-space(text())='{text}']"
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(f'Step failed. Element with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

@then('Verify partial text "{text}" is available')
def verify_partial_text(context, text):
    xpath = f"//*[contains(text(), '{text}')]"
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(f'Step failed. Element with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

