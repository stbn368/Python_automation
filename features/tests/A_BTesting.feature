Feature: A/B Testing

  Scenario: Verify a text after clicking on the "A/B Testing" link
    When Click on the link with text "A/B Testing"
    Then Verify exact text "A/B Test Variation 1" is available
    Then Verify partial text "This is a way in which businesses are able to simultaneously" is available

