# Created by ysafr at 1/22/2021

Feature: Amazon Search Item

  Scenario: Add Item to the cart and then delete it and verify tht cart is empty
#The Mandalorian
    Given Go to Amazon
    When Enter The Mandalorian
    And Click Enter
    And Choose Item and Click on it
    Then Add Item to the cart
    And Go to Cart
    And DropDown Menu open
    And Change to zero
    And Check Cart
    And Verify that Cart is Empty