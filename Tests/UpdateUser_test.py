import allure
from RequestBase.RequestMethods import Requests
from Validator.Asserts import Asserts 
from Utils.Config import Properties


PATH = "/api/users/"

@allure.description("Update user with success and validate status code and response json")
def test_update_user_success():
    ID = "2"
    pload = {'name':'Ramon','job':'QA Automation'}
    request = Requests()
    response = request.execute_put_request(Properties.BASE_URL+PATH+ID, pload)
    response_body = response.json()
    
    validator = Asserts()
    validator.validate_status_code(200, response.status_code)
    validator.validate_response("Ramon", response_body["name"])    
    validator.validate_response("QA Automation", response_body["job"])     