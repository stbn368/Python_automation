from behave import *
from selenium.webdriver.common.by import *

@when('Click on the link with text "{text}"')
def click_link_text(context, text):
    try:
        xpath = f"//a[normalize-space(text())='{text}']" 
        link = context.driver.find_element(By.XPATH, xpath)
        link.click()
    except Exception as e:
        print(f'Step failed. Link with text {text} does not found. {type(e).__name__} - {str(e)}')
        raise

