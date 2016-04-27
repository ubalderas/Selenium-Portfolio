*** Settings ***
Library         Selenium2Library
Suite Setup     Suite Start
Test Teardown   Test Complete
Suite Teardown  Close All Browsers

*** Variables ***
${BROWSER}                  firefox
${w3SchoolsUrl}             http://www.w3schools.com/
${w3SchoolsLogo}            //a[@class='w3schools-logo' and @href='http://www.w3schools.com']
${htmlRowLocator}           //div[@class='w3-row']//h1[.='HTML']/..
${cssRowLocator}            //div[contains(@class,'w3-row')]//h1[.='CSS']/..
${javascriptRowLocator}     //div[@class='w3-row']//h1[.='JavaScript']/..
${sqlRowLocator}            //div[@class='w3-row w3-light-grey']//h2[.='SQL']/..
${phpRowLocator}            //div[@class='w3-row w3-light-grey']//h2[.='PHP']/..
${jQueryRowLocator}         //div[@class='w3-row w3-light-grey']//h2[.='jQuery']/..
${w3CssRowLocator}          //div[@class='w3-row']//h2[.='W3.CSS']/..
${colorPickerRowLocator}    //div[@class='w3-row']//h2[.='Color Picker']/..
${bootstrapRowLocator}      //div[@class='w3-row']//h2[.='Bootstrap']/..

*** Keywords ***
w3Schools Page Should be Open
    Wait until element is visible   ${w3SchoolsLogo}
    Element should contain          ${w3SchoolsLogo}    w3schools

Suite Start
    Open Browser    ${w3SchoolsUrl}   browser=${BROWSER}
    w3Schools Page Should be Open

Test Complete
    Go To   ${w3SchoolsUrl}
    w3Schools Page Should be Open

Scroll Element into View
    [Documentation]     Scrolls an element into view, it requires a locator, and the locator type (CSS ,XPATH, ID)
    [Arguments]     ${locator}      ${locatorType}
    Run Keyword if      '${locatorType}'=='ID'        Execute Javascript      document.getElementById('${locator}').scrollIntoView()
    ...     ELSE IF     '${locatorType}'=='CSS'       Execute Javascript      document.querySelector('${locator}').scrollIntoView()
    ...     ELSE IF     '${locatorType}'=='XPATH'
    ...                 Execute Javascript      document.evaluate("${locator}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()
    ...     ELSE        FAIL    Locator Type is invalid

Wait until visible and Scroll into Element
    [Arguments]     ${locator}      ${locatorType}
    Page should contain element     ${locator}
    Scroll Element into View        ${locator}      ${locatorType}
    Element should be visible       ${locator}

Validate Home Page Content
    Wait until visible and Scroll into Element      ${htmlRowLocator}               XPATH
    Element should contain                          ${htmlRowLocator}//p            The language for building web pages
    Wait until visible and Scroll into Element      ${cssRowLocator}                XPATH
    Element should contain                          ${cssRowLocator}//p             The language for styling web pages
    Wait until visible and Scroll into Element      ${javascriptRowLocator}         XPATH
    Element should contain                          ${javascriptRowLocator}//p      The language for programming web pages
    Wait until visible and Scroll into Element      ${sqlRowLocator}                XPATH
    Element should contain                          ${sqlRowLocator}//p             A language for accessing databases

*** Test Cases ***
Simple Navigation to w3Schools
    Validate Home Page Content
