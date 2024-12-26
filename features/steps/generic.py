from behave import *
from selenium.webdriver.common.by import *

@given('Select the option "{text}" in the home page')
def select_option(context, text):
    try:
        option_xpath = f"//div/h5[text()='{text}']"
        option = context.driver.find_element(By.XPATH, option_xpath)
        option.click()
    except Exception as e:
        print(f'Step failed. Select the option {text} in the home page. {type(e).__name__} - {str(e)}')
        raise

@given('Select the element with text "{text}" in the list')
def select_element_list(context, text):
    try:
        element_xpath = f"//li/span[text()='{text}']"
        element = context.driver.find_element(By.XPATH, element_xpath)
        element.click()
    except Exception as e:
        print(f'Step failed. Select the element with text "{text}" in the list. {type(e).__name__} - {str(e)}')
        raise
