import allure
from RequestBase.RequestMethods import Requests
from Validator.Asserts import Asserts 
from Utils.Config import Properties
from Utils.ProjectUtils import Utils


PATH = "/api/users/"

@allure.description("Update user with success and validate status code and response json")
def test_update_user_success():
    ID = "2"
    FILE_NAME = "./Schemas/UpdateUser.json"
    file = Utils()
    pload = file.load_json_file_content(FILE_NAME)

    request = Requests()
    response = request.execute_put_request(Properties.BASE_URL+PATH+ID, pload)
    response_body = response.json()
    
    validator = Asserts()
    validator.validate_status_code(200, response.status_code)
    validator.validate_response("morpheus", response_body["name"])    
    validator.validate_response("zion resident", response_body["job"])     