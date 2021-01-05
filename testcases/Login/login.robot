*** Settings ***
Resource            ../../imports.robot

Test Setup      run keywords
                    ...   Open app
                    ...   Login


*** Test Cases ***
tc_01 - login success
