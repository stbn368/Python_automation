Feature: Verify Element on the Page
  As a user, I want to verify the presence of a specific element on the home page.

  Scenario Outline: Check for specific element
    Given I navigate to the home page
    Then I should see the element "<element_selector>" on the page

    Examples:
      | element_selector |
      | h1               |
      | div              |

