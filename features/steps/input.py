from behave import *
from selenium.common.exceptions import *
from selenium.webdriver.common.by import *

@when('I fill the input with id "{input_id}" with "{value}"')
# Step to fill an input element using the id
def fill_input(context, input_id, value):
    context.driver.find_element("id", input_id).clear().send_keys(value)

@then('Page specific: Log in with username "{username}" and password "{password}"')
# Step to log in with username and password
def enter_text_field(context, username, password):
    locator_success_auth = f"//*[contains(text(), 'Congratulations! You must have the proper credentials.')]"
    try:
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        context.driver.get(url)
        context.driver.find_element(By.XPATH, locator_success_auth)
    except NoSuchElementException as e:
        print(f'Step failed. Log in failed. {type(e).__name__} - {str(e)}')
        raise
