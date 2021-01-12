*** Settings ***
Resource            ../../imports.robot


*** Keywords ***
input username adr
    [Arguments]         ${username}
    input text          ${adr_input_username}          ${username}

input password adr
    [Arguments]         ${password}
    input value          ${adr_input_password}         ${password}

click login button adr
   Click Element            ${adr_btn_login}

verify error message adr
    [Arguments]     ${err_message}
    Wait Until Element Is Visible       ${adr_txt_error}          ${min_time_out}
    ${txt_error}=    Get Text       ${adr_txt_error}
    Should Be Equal      ${txt_error}       ${err_message}


clear username and password text adr
    Wait until element is visible       ${adr_input_username}           ${min_time_out}
    Clear Text      ${adr_input_username}
    Clear Text      ${adr_input_password}

login success
    [Arguments]         ${username}=${valid_username_1}       ${password}=${valid_password_1}
    input username              ${username}
    input password              ${password}
    click login button

invalid login adr
    [Arguments]     ${username}      ${password}        ${err_message}
    clear username and password text adr
    input username adr             ${username}
    input password adr             ${password}
    click login button adr
    verify error message adr       ${err_message}