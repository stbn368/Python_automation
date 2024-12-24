Feature: Text box interactions

  Scenario: Complete the text box fields
    Given Select the option "Elements" in the home page
    Then Verify exact text "Please select an item from left to start practice." is available
    Given Select the element with text "Text Box" in the list
    Then Verify exact text "Full Name" is available

