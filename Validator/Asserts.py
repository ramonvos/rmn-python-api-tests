import allure

class Asserts():

    # def __init__(self) -> None:
    #     pass
      
    @allure.step("Validade Status Code")
    def validate_status_code(self, expected,actual):
        assert expected == actual
        
    @allure.step("Validade Response")
    def validate_response(self, expected,actual):
        assert expected == actual
        