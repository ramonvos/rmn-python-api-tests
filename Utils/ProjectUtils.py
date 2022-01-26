
class Utils():

    def load_json_file_content(self, jsonPath, fileName):
        file = open(jsonPath+fileName,'r')
        json_input = file.read()
        return json_input