*** Variables ***

${retry_time}                           2s
${min_time_out}                         5s
${avg_time_out}                         15s


#setup devices
${no_reset}                                 true
${auto_grant_permissions}                   true
${new_command_timeout}                      1800
${platform_name_ios}                        iOS
${platformNameAndroid}                      Android

${app}                                      org.reactjs.native.example.SwagLabsMobileApp
${app_package}                              com.swaglabsmobileapp
${app_file}                                 /Users/giauthe/Documents/Pythonn Practice/resources/SauceLabs.Mobile.apk
${app_wait_activity}                        com.swaglabsmobileapp.MainActivity

${device_name_ios_1}                        iPhone 8 Plus
${platform_version_ios_1}                   13.3

${device_name_android_1}                    android test
${platform_version_android_1}               9.0



