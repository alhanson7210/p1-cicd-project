Feature: Test Given GH Test Uri Endpoint
  As a student in deploying working software,
  I want to test the secrets given by a gh action,
  So that the correct endpoint is used for testing

  Scenario: Test Uri Endpoint Given Via Env Var
    When I wish to test the endpoint from the test uri given by the gh action secret
    Then the response status code should be 200

