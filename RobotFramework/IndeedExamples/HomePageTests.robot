*** Settings ***
Resource    resources.robot
Suite Setup         Open Browser to www.indeed.com using Firefox
Suite Teardown      Close all Browsers
Test Teardown       Go To   www.indeed.com
*** Variables ***


*** Test Cases ***
Validate Home Page Content
    Home page should be loaded
    Validate Form content
    Validate Welcome Message content
    Validate Global Navigation content
    Validate Footer content