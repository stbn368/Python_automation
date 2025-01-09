from behave import *
from selenium.webdriver.common.by import *
from features.configuration import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@when('Click on the link with text "{text}"')
# Step to click on a link element using the text present in the element
def click_link_text(context, text):
    try:
        xpath = f"//a[normalize-space(text())='{text}']" 
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(
            ec.element_to_be_clickable((By.XPATH, xpath))).click()
    except Exception as e:
        print(f'Step failed. Link with text {text} was not found. {type(e).__name__} - {str(e)}')
        raise

