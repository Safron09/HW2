# Created by ysafr at 1/22/2021


Feature: Scenario for Checking if shopping cart is empty

  Scenario: Check if shopping cart is empty

    Given Go to Amazon WebPage
    When Click on Cart Icon
    Then Check If cart is empty


