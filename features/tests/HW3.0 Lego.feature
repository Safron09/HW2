# Created by ysafr at 1/21/2021
Feature: #Lego Search

  Scenario: Verify the search was correct

    #Steps to execute
    Given Open Amazon web page
    When Fill input string Pool
    And Click Search button
    Then Verify that It searched for Pool
