Feature: Basic Auth option

  Scenario: Verify a basic authentication
    When Click on the link with text "Basic Auth"
    Then Page specific: Log in with username "admin" and password "admin"
