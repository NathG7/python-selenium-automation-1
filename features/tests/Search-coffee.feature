Feature: Target main page search tests

Scenario: User can search for a coffee  on target
    Given Open target main page
    When Search for coffee
    Then Verify search results show for coffee


