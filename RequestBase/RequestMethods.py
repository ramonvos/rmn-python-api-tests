import requests
import allure

class Requests():
    @allure.step("Execute Get Request")
    def execute_get_request(self,url):
        response = requests.get(url)
        print(url)
        print(response.status_code)
        print(response.text)
        allure.attach(str(response.status_code),name="StatusCode",attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text,name="ResponseBody",attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("Execute Post Request")
    def execute_post_request(self,url,requestBody):
        response = requests.post(url, data=requestBody)
        allure.attach(str(response.status_code),name="StatusCode",attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text,name="ResponseBody",attachment_type=allure.attachment_type.TEXT)
        return response
    
    @allure.step("Execute Put Request")
    def execute_put_request(self,url,requestBody):
        response = requests.put(url, data=requestBody)
        allure.attach(str(response.status_code),name="StatusCode",attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text,name="ResponseBody",attachment_type=allure.attachment_type.TEXT)
        return response
    
    @allure.step("Execute Delete Request")
    def execute_delete_request(self,url):
        response = requests.delete(url, )
        allure.attach(str(response.status_code),name="StatusCode",attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text,name="ResponseBody",attachment_type=allure.attachment_type.TEXT)
        return response