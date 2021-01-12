*** Settings ***
Resource            ../../imports.robot


*** Keywords ***
input username
    [Arguments]         ${username}
    input text          ${input_username}          ${username}

input password
    [Arguments]         ${password}
    input value          ${input_password}         ${password}

click login button
   Click Element            ${btn_login}

verify error message
    [Arguments]     ${err_message}
    Wait Until Element Is Visible       ${err_message}          ${min_time_out}

clear username and password text
    Clear Text      ${input_username}
    Clear Text      ${input_password}

login success
    [Arguments]         ${username}=${valid_username_1}       ${password}=${valid_password_1}
    input username              ${username}
    input password              ${password}
    click login button

invalid login
    [Arguments]     ${username}      ${password}        ${err_message}
    clear username and password text
    input username              ${username}
    input password              ${password}
    click login button
    verify error message        ${err_message}