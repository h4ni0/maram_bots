from requests import get, post

class ApiUtils:
    def __check_status(self, status_code):
        if status_code < 200 or status_code >= 400:
            raise Exception(f"Error while making a get request, error code: {status_code}")

    def __get_response(slef, response, return_type):
        match return_type:
            case "text":
                return response.text
            case "json":
                return response.json()
            case "content":
                return response.content
            case "cookies":
                return response.cookies
            case _:
                raise Exception(f"Unkown return type {return_type}")

    def get(self, url, return_type="text"):
        resposne = get(url, timeout=20)
        self.__check_status(response.status_code)
        self.__get_response(response, return_type)
        
    def post(self, url, payload=None):
        response = post(url, data=payload)
        self.__check_status(response.status_code, timeout=20)
        self.__get_response(response, return_type)
