#!/usr/bin/env bash
ENV="qa"
#BASE_REPOS="acm-orbit-irs-base-functional-test"
RESULT_FOLDER="../../results/$ENV"
TESTCASE_FOLDER="../../testcases/"

## We run the update commands only when there is new version of python or other dependencies
## command for update apt-get
#apt-get update -y
#
### install python-dev for fix error when install pycrypto
#apt-get install -y python-dev

## install virtualenv
#pip3 install virtualenv

## create virtualenv for run robot
#virtualenv virtualenv

## use "." instead of "source" because os is ubuntu to activate env
#. virtualenv/bin/activate

## delete screenshot.png before running robot
#rm -rf ../../selenium-screenshot*.png
#rm -rf $RESULT_FOLDER/selenium-screenshot*.png

## We just need to install Robot libraries in script of BASE REPOS only
#echo "=== $(date) - Installing robot libraries in file requirement.txt ==="

## We only install robot libs in the base repos so we don't need here
pip3 install -r requirements.txt
#pip3 list
#echo "=== $(date) Finished installation !!! Done !!! ==="


## Commands to run robot and rerun the failed test cases
echo "=== $(date) - TRANSACTION CONFIRMATION - STAGING - Running main job === "
python3 -m robot.run -L TRACE -v ENV:$ENV -v browser:headlesschrome -e ignore -e not-ready -d $RESULT_FOLDER $TESTCASE_FOLDER
#python3 -m robot.run -L TRACE -v ENV:$ENV -v browser:headlesschrome -e ignore -e not-ready test.robot
echo "=== $(date) - TRANSACTION CONFIRMATION - STAGING - Finished main job !!! Done !!! === "

#echo "=== Running rerun job with failed test cases ==="
#python3 -m robot.run -v env:$ENV --rerunfailed $RESULT_FOLDER/output.xml --output $RESULT_FOLDER/rerun.xml $TESTCASE_FOLDER
#date
#python3 -m robot.rebot --merge --output $RESULT_FOLDER/output.xml $RESULT_FOLDER/output.xml $RESULT_FOLDER/rerun.xml
#date

exit 0