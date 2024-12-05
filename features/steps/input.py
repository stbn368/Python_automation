from behave import when

@when('I fill the input with id "{input_id}" with "{value}"')
def fill_input(context, input_id, value):
    input_element = context.driver.find_element("id", input_id)
    input_element.clear()
    input_element.send_keys(value)
