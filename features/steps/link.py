from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import *

@when('Click on the link with text "{link_text}"')
def click_link_text(context, link_text):
    try:
        xpath = f"//a[normalize-space(text())='{link_text}']" 
        link = context.driver.find_element(By.XPATH, xpath)
        link.click()
    except Exception as e:
        print(f'Step failed. Link with text {link_text} does not found. {type(e).__name__} - {str(e)}')
        raise

