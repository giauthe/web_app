*** Settings ***
Resource             ../../imports.robot
#Library              DataDriver     ../../testdata/LoginData/login_data.xlsx   sheet_name=Sheet1
Library              DataDriver   ../../testdata/LoginData/login_data.csv

Suite Setup         Open SwagLabsMobileApp on android emulator
Suite Teardown      Close Application
Test Template       invalid login


*** Keywords ***
invalid login
    [Arguments]     ${username}      ${password}        ${err_message}
    clear username and password text adr
    input username adr             ${username}
    input password adr             ${password}
    click login button adr
    verify error message adr       ${err_message}


*** Test Cases ***
#Right user empty pass           problem_user                    ${empty}                    ${txt_err_password_message}
#Right user wrong pass           problem_user                    problem_user                ${txt_err_username_password_message}
#Wrong user right pass           problem_uses                    secret_sauce                ${txt_err_username_password_message}
#Wrong user empty pass           problem_uses                    ${empty}                    ${txt_err_password_message}
#Wrong user wrong pass           problem_uses                    problem_user                ${txt_err_username_password_message}


#tc_bdd
#   [Tags]   login     already_test
#    Given clear username and password text
#    When input username             problem_user
#    And input password             ${empty}
##    Pause Execution
#    And click login button
#    Then verify error message       ${txt_err_password_message}

TC Adnroid - ${tcname}