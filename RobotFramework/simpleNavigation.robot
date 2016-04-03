*** Settings ***
Library     Selenium2Library

*** Variables ***
${ENTER_KEY}    \\13

*** Keywords ***
Open Browser to ${url} using ${browser}
    Open Browser    http://${url}   browser=${browser}
    title should be     Welcome to Python.org


*** Test Cases ***
Simple Navigation to Python Page
    Open Browser to www.python.org using firefox
    Input text  q   pycon
    Press Key   q   ${ENTER_KEY}
    wait until page contains    Results
    Page should not contain     No results found.
    close all browsers