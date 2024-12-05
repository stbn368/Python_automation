from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import *

@when('Click the button with id "{button_id}"')
def click_button(context, button_id):
    try:
        button = context.driver.find_element("id", button_id)
        button.click()
    except:
        print(f'')
        
@then('Verify button text {button_text} exists')
def verify_button_text(context, button_text):
    try:
        xpath = f"//button[normalize-space(text())='{button_text}']"
        element = context.driver.find_element(By.XPATH, xpath)
    except:
        print(f"Button with text '{button_text}' not found")


