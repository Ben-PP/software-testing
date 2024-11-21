*** Settings ***

Library  Browser
Resource    common.resource

*** Variables ***

${USERNAME}    demo
${VALID_PASSWORD}    mode

*** Keywords ***

Verify That Welcome Page Is Visible
    Get Title    Equals    Welcome Page

Do Successful Logout
    Click    text=logout
Verify That Login Page Is Visible
    Get Title    Equals    Login Page

Do Successful Login
    Open Browser To Login Page
    Enter Username    ${USERNAME}
    Enter Password    ${VALID_PASSWORD}
    Submit Login Form

*** Test Cases ***

Welcome page should be visible after successful login
    [Setup]    Do Successful Login
    Verify That Welcome Page Is Visible
    [Teardown]    Do Successful Logout

Login Form Should Be Visible After Successful Logout
    [Setup]    Do Successful Login
    Verify That Welcome Page Is Visible
    Do Successful Logout
    Verify That Login Page Is Visible