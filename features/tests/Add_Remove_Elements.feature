Feature: Add/Remove button elements

  Scenario: Add and remove the button elements
    When Click on the link with text "Add/Remove Elements"
    Then Verify exact text "Add/Remove Elements" is available
    Then Verify button text "Add Element" exists
    When Click the button with text "Add Element"
    Then Verify button text "Delete" exists

