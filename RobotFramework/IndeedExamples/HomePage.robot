*** Settings ***
Resource    resources.robot


*** Keywords ***
Open Browser to ${url} using ${browser}
    Open Browser    http://${url}   browser=${browser}
    Maximize Browser Window

Home page should be loaded
    :FOR    ${element}  IN  @{HOME_PAGE_MAIN_ELEMENTS}
    \   wait until element is visible   ${element}

Validate Form content
    :FOR    ${element}  IN  @{HOME_PAGE_FORM_ELEMENTS}
    \   wait until element is visible   ${element}

Validate Welcome Message content
    :FOR    ${element}  IN  @{HOME_PAGE_WELCOME_ELEMENTS}
    \   wait until element is visible   ${element}

Validate Global Navigation content
    :FOR    ${element}  IN  @{HOME_PAGE_GLOBAL_NAV_ELEMENTS}
    \   wait until element is visible   ${element}

Validate Footer content
    :FOR    ${element}  IN  @{HOME_PAGE_FOOTER_ELEMENTS}
    \   wait until element is visible   ${element}