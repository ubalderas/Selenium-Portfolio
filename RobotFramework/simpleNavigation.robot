*** Settings ***
Library     Selenium2Library

*** Keywords ***
Open Browser to ${url} using ${browser}
    Open Browser    http://${url}   browser=${browser}
    title should be     Welcome to Python.org
    close all browsers

*** Test Cases ***
Simple Navigation to Python Page
    Open Browser to www.python.org using firefox