*** Settings ***

Library              AppiumLibrary
Library              String
Library              Collections
Library              Dialogs
Library              ./keywords/common/Common.py

# elements
Resource             ./elements/CommonElements.robot
Resource             ./elements/LoginPage.robot


# keywords
Resource             ./keywords/common/CommonUtils.robot
Resource             ./keywords/page/LoginPageIos.robot
Resource             ./keywords/page/LoginPageAndroid.robot

# config
Variables            ./config_${env}.yaml

#variable
Resource             ./variables/common.robot
Resource             ./variables/login.robot

