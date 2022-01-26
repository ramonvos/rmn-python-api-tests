import allure
from RequestBase.RequestMethods import Requests
from Validator.Asserts import Asserts 
from Utils.Config import Properties


PATH = "/api/users/"

@allure.description("Delete user with success and validate status code and response json")
def test_delete_user_success():
    ID = "2"
    request = Requests()
    response = request.execute_delete_request(Properties.BASE_URL+PATH+ID)
    
    validator = Asserts()
    validator.validate_status_code(204, response.status_code)
