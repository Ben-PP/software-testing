*** Settings ***

Library  Browser

*** Variables ***

${username}    demo
${password}    mode

*** Test Cases ***

Welcome page should be visible after successful login
    New Browser    headless=${FALSE}
    New Page    http://localhost:7272
    Type Secret    id=username_field    secret=$username
    Type Secret    id=password_field    secret=$password
    Click    id=login_button
    Get Title    Equals    Welcome Page