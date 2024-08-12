Feature: Target cart

#  Scenario: Verify cart is empty
#    Given Open target main page
#    When click on cart
#    Then verify cart is empty

  Scenario: Add items to cart and verify
    Given Open target main page
    When search for coffee
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from the side navigation
    And Open cart page
    Then Verify cart has item(s)




