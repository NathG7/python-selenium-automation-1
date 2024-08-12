Feature: Target main page search tests

Scenario Outline: User can search for a product on target
    Given Open target main page
    When Search for <product>
    Then Verify search results show for <product>
  Examples:
  |product |product   |
  |coffee  |coffee    |
  |tea     |tea       |
  |iphone  |iphone    |

