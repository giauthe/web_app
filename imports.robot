*** Settings ***
# library
Library           Selenium2Library
Library           AppiumLibrary
Library           String
Library           Collections
Library           ./keywords/common/Common.py

# elements
Resource          ./elements/CommonElements.robot
Resource          ./elements/HomePage.robot



# keywords
Resource          ./keywords/common/CommonUtils.robot
Resource          ./keywords/page/LoginRegisterUserPage.robot


# config
Variables         ./config_${env}.yaml

#variable
Resource          ./variables/common.robot
Resource          ./variables/login.robot
Resource          ./variables/setup_device.robot
