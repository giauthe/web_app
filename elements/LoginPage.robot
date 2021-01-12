*** Variables ***

${input_username}                             name=test-Username
${input_password}                             name=test-Password
${btn_login}                                  name=test-LOGIN
${txt_err_username_password_message}          Username and password do not match any user in this service.
${txt_err_username_message}                   Username is required
${txt_err_password_message}                   Password is required


${adr_input_username}                             xpath=//android.widget.EditText[@content-desc="test-Username"]
${adr_input_password}                             xpath=//android.widget.EditText[@content-desc="test-Password"]
${adr_btn_login}                                  xpath=//android.view.ViewGroup[@content-desc="test-LOGIN"]
${adr_txt_err_username_password_message}          Username and password do not match any user in this service.
${adr_txt_err_username_message}                   Username is required
${adr_txt_err_password_message}                   Password is required
${adr_txt_error}                                  xpath=//android.view.ViewGroup[@content-desc="test-Error message"]/android.widget.TextView


