*** Settings ***
Resource            ../../imports.robot

*** Keywords ***
Common - Verify Element text
    [Arguments]         ${element_lct}      ${element_text}
    Wait Until Keyword Succeeds     20s     5s          Element Should Be Visible          ${element_lct}
    Element Text Should Be          ${element_lct}          ${element_text}

Common - Verify checkbox is checked
    [Arguments]     ${element}
    ${checkbox_state}       Get Element Attribute           ${cbx_input_add}            checked
    should be equal as strings          ${checkbox_state}       true

Common - Verify checkbox is unchecked
    [Arguments]     ${element}
    ${checkbox_state}       Get Element Attribute           ${cbx_input_add}            checked
    should be equal as strings          ${checkbox_state}       false










