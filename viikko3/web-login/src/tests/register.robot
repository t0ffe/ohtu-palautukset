*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and contain only lowercase letters a-z

Register With Valid Username And Too Short Password
    Set Username  validname
    Set Password  short1
    Set Password Confirmation  short1
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  validname
    Set Password  invalidpwd
    Set Password Confirmation  invalidpwd
    Submit Credentials
    Register Should Fail With Message  Password must not consist solely of letters

Register With Nonmatching Password And Password Confirmation
    Set Username  validname
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is already taken

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
