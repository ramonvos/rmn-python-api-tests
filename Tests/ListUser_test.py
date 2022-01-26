import allure
from RequestBase.RequestMethods import Requests
from Validator.Asserts import Asserts 
from Utils.Config import Properties


PATH = "/api/users/"

@allure.description("List all users with success and validate status code and response json")
def test_list_all_user_success():
    request = Requests()
    response = request.execute_get_request(Properties.BASE_URL+PATH)
    response_body = response.json()

    validator = Asserts()
    validator.validate_status_code(200, response.status_code)
    validator.validate_response(1, response_body["data"][0]["id"])  
    validator.validate_response("george.bluth@reqres.in", response_body["data"][0]["email"])  

@allure.description("List user by id with success and validate status code and response json")
def test_list__user_by_id_success():
    ID = "2"
    request = Requests()
    response = request.execute_get_request(Properties.BASE_URL+PATH+ID)
    response_body = response.json()

    validator = Asserts()
    validator.validate_status_code(200, response.status_code)
    validator.validate_response(2, response_body["data"]["id"])  
    validator.validate_response("janet.weaver@reqres.in", response_body["data"]["email"])  