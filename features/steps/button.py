from behave import *
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.configuration import Config
#import time

def find_button_xpath(text):
# Function to find the xpath of a button element using the text present in the element
    xpath_list = [
                  f"//button[normalize-space(text())='{text}']",
                  f"//input[@class='button' and @value='{text}']"
                  ]
    return ' | '.join(xpath_list)


@when('Click the button with id "{button_id}"')
# Step to click on a button element using the id
def click_button(context, button_id):
    try:
        button = context.driver.find_element("id", button_id)
        button.click()
    except Exception as e:
        print(f'Step failed. Could not click button with id "{button_id}". {type(e).__name__} - {str(e)}')
        raise


@when('Click the button with text "{text}"')
# Step to click on a button element using the text present in the element
def click_button_text(context, text):
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.element_to_be_clickable((By.XPATH, find_button_xpath(text)))).click()
        #time.sleep(10)
    except Exception as e:
        print(f'Step failed. {type(e).__name__} - {str(e)}')
        raise


@when('Verify button text "{text}" exists')
# Step to verify if a button exists looking for the text in the button
def verify_button_text(context, text):
    try:
        WebDriverWait(context.driver, Config.EXPLICIT_WAIT).until(ec.presence_of_element_located((By.XPATH, find_button_xpath(text))))
    except Exception as e:
        print(f'Step failed. Could not click button with text "{text}". {type(e).__name__} - {str(e)}')
        raise
