*** Settings ***
Resource            ../../imports.robot

*** Keywords ***

Open SwagLabsMobileApp on ios emulator
        [Arguments]      ${device_name}=${device_name_ios_1}            ${platform_version}=${platform_version_ios_1}
         Open Application
            ...  ${address}
            ...  autoGrantPermissions=${auto_grant_permissions}
            ...  newCommandTimeout=${new_command_timeout}
            ...  platformVersion=${platform_version}
            ...  platformName=${platform_name_ios}
            ...  deviceName=${device_name}
            ...  noReset=${no_reset}
            ...  app=${app}

Open SwagLabsMobileApp on ios real device
        [Arguments]     ${device_name}=${device_name_ios_1}            ${platform_version}=${platform_version_ios_1}
         Open Application
            ...  ${address}
            ...  autoGrantPermissions=${auto_grant_permissions}
            ...  newCommandTimeout=${new_command_timeout}
            ...  platformVersion=${platform_version}
            ...  platformName=${platform_name_ios}
            ...  deviceName=${device_name}
            ...  noReset=${no_reset}
            ...  udid=${udid}
            ...  app=${app}

Open SwagLabsMobileApp on android emulator
        [Arguments]      ${device_name}=${device_name_android_1}            ${platform_version}=${platform_version_android_1}
         Open Application
            ...  ${address}
            ...  autoGrantPermissions=${auto_grant_permissions}
            ...  newCommandTimeout=${new_command_timeout}
            ...  platformVersion=${platform_version}
            ...  platformName=${platformNameAndroid}
            ...  deviceName=${device_name}
            ...  noReset=${no_reset}
            ...  app=${app_file}
            ...  appPackage=${app_package}
            ...  appWaitActivity=${app_wait_activity}




Common - Verify Element text
    [Arguments]         ${element_lct}      ${element_text}
    Wait Until Keyword Succeeds     20s     5s          Element Should Be Visible          ${element_lct}
    Element Text Should Be          ${element_lct}          ${element_text}         ${retry_time}

Common - Verify checkbox is checked
    [Arguments]     ${element}
    ${checkbox_state}       Get Element Attribute           ${cbx_input_add}            checked
    should be equal as strings          ${checkbox_state}       true

Common - Verify checkbox is unchecked
    [Arguments]     ${element}
    ${checkbox_state}       Get Element Attribute           ${cbx_input_add}            checked
    should be equal as strings          ${checkbox_state}       false










