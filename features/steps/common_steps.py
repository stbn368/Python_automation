from behave import given, then
from pom.home_page import HomePage

@given('I navigate to the home page')
def step_navigate_home(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate()

@then('I should see the title "{title}"')
def step_verify_title(context, title):
    assert title in context.driver.title, f"Expected title '{title}' not found."

@then('I should see the element "{element_selector}" on the page')
def step_verify_element(context, element_selector):
    assert context.home_page.is_element_present(element_selector), f"Element '{element_selector}' not found on the page."
