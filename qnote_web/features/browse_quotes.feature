Feature: Browse quotes homepage
    As a normal visitor
    I would like to browse all quotes

    Scenario: Browse quotes homepage
        Given there are "100" quotes in the system
        When I visit "/"
        Then I should see a list of quotes