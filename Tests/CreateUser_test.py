import allure
from RequestBase.RequestMethods import Requests
from Validator.Asserts import Asserts 
from Utils.Config import Properties
from Utils.ProjectUtils import Utils

PATH = "/api/users/"

@allure.description("Create new user with success and validate status code and response json")
def test_create_new_user_success():
    FILE_NAME = "./Schemas/CreateUser.json"
    file = Utils()
    pload = file.load_json_file_content(FILE_NAME)
    request = Requests()
    response = request.execute_post_request(Properties.BASE_URL+PATH, pload)
    response_body = response.json()
  
    validator = Asserts()
    validator.validate_status_code(201, response.status_code)
    validator.validate_response("Ramon", response_body["name"])    
    validator.validate_response("QA Lead", response_body["job"])     