# Invalid credential possibilities
# - No username
# - No password
# - Invalid username
# - Invalid password
# - No username & Invalid password
# - Invalid username & No Password

*** Settings ***

Library  Browser
Resource    common.resource

Test Setup    Open Browser To Login Page
Test Template    Error Page Is Visible When Using Incorrect Credentials

*** Variables ***


${VALID_USERNAME}    demo

${VALID_PASSWORD}    mode

*** Keywords ***

Verify That Error Page Is Visible
    Get Title    Equals    Error Page

Error Page Is Visible When Using Incorrect Credentials
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Submit Login Form
    Verify That Error Page Is Visible

*** Test Cases ***
# Test case name               # Username     #Password
Empty Username Empty Password    ${EMPTY}    ${EMPTY}
Empty Username Valid Password    ${EMPTY}     ${VALID_PASSWORD}
Valid Username Empty Password    ${VALID_USERNAME}    ${EMPTY}
Valid Username Invalid Password    ${VALID_USERNAME}    Incorrect
Invalid Username Valid Password    invalid    ${VALID_PASSWORD}
