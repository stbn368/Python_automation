Feature: DinamicID Element Interactions

  Scenario: Verify button after clicking on the Dynamic ID element
    Then Verify exact text "Dynamic ID" is available
    When Click on the link with text "Dynamic ID"
    Then Verify button text "Button with Dynamic ID" exists