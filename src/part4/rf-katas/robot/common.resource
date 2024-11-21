*** Settings ***

Library  Browser

*** Variables ***

${URL}    http://localhost:7272

*** Keywords ***

Open Browser To Login Page
    New Browser    headless=${TRUE}
    New Page    ${URL}

Enter Username
    [Arguments]    ${username}
    Fill Text    id=username_field    txt=${username}

Enter Password
    [Arguments]    ${password}
    Fill Secret    id=password_field    secret=$password

Submit Login Form
    Click    id=login_button