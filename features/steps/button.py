from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import *

@when('Click the button with id "{button_id}"')
# Step to click on a button element using the id
def click_button(context, button_id):
    try:
        button = context.driver.find_element("id", button_id)
        button.click()
    except Exception as e:
        print(f'Step failed. {type(e).__name__} - {str(e)}')
        raise
        
@then('Verify button text {text} exists')
# Step to verify if a button exists looking for the text in the button
def verify_button_text(context, text):
    try:
        xpath = f"//button[normalize-space(text())='{text}']"
        element = context.driver.find_element(By.XPATH, xpath)
    except Exception as e:
        print(f'Step failed. {type(e).__name__} - {str(e)}')


