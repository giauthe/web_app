*** Settings ***
Resource            ../../imports.robot

*** Keywords ***
Register User - Validate "Register User" screen is displayed
    Wait Until Keyword Succeeds          30s     5s          Page Should Contain Text                ${txt_register_new_user}
    Common - Press Back button
    Element Text Should Be                              ${lbl_user_name_locator}        ${lbl_user_name_text}
    Element Should Be Visible                           ${ipt_user_name}
    Page Should Contain Text                            ${lbl_email}
    Element Should Be Visible                           ${ipt_email}
    Page Should Contain Text                            ${lbl_password}
    Element Should Be Visible                           ${ipt_password}
    Common - Swipe Down
    Page Should Contain Text                            ${lbl_Name}
    Element Should Be Visible                           ${ipt_name}
    Page Should Contain Text                            ${lbl_programming_lang}
    Element Should Be Visible                           ${drd_program_language}
    Element Should Be Visible                           ${cbx_input_add}
    Element Should Be Visible                           ${btn_register}
    Common - Verify checkbox is unchecked               ${cbx_input_add}

Register User - Input valid info and click Register button
    Input Text              ${ipt_user_name}            user name
    Input Text              ${ipt_email}                email
    Input Text              ${ipt_password}             password
    Clear Text              ${ipt_name}
    Input Text              ${ipt_name}                 name
#    Common - Press Back button
    Common - Click Element          ${drd_program_language}
    Wait Until Page Contains Element        ${top_programing_language}
    Common - Click Element          ${txt_python}
    Common - Click Element          ${cbx_input_add}
    Common - Click Element          ${btn_register}

Login - Input phone number
     [Arguments]             ${phone_number_lct}         ${phone_number}
     Input Text              ${phone_number_lct}             ${phone_number}

Login - Input password
      [Arguments]            ${password_lct}             ${password}
      Input Text             ${password_lct}                 ${password}

Login
      [Arguments]           ${phone_number}=${valid_phone_number}             ${password}=${valid_password}
      Login - Input phone number           ${ipt_so_dien_thoai}               ${phone_number}
      Login - Input password               ${ipt_mat_khau}                    ${password}
