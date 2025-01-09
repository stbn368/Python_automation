from behave import then
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.configuration import Config
from selenium.common.exceptions import TimeoutException
    
@then('Verify exact text "{text}" is available')
# Step to verify if the exact text is available in the page
def verify_text(context, text):
    xpath = f"//*[normalize-space(text())='{text}']"
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(f'Step failed. Element with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

@then('Page specific: Verify exact text "{text}" is available or another one if it fails')
# This step is used to verify a specific text in a page. If the text is not found, it will try to find another one.
def verify_text(context, text):
    xpath = f"//*[normalize-space(text())='{text}']"
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException as e:
        print("First element was not found. Trying with another one.")
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.visibility_of_element_located((By.XPATH, "//*[normalize-space(text())='A/B Test Control']")))
    except Exception as e:
        print(f'Step failed. Element with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

@then('Verify partial text "{text}" is available')
# Step to verify if the partial text is available in the page
def verify_partial_text(context, text):
    xpath = f"//*[contains(text(), '{text}')]"
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(f'Step failed. Element with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

