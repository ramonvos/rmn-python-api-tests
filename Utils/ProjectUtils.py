
import json
class Utils():

    def load_json_file_content(self, filename):
         # Read the file
        with open(str(filename)) as config_file:
            config = json.load(config_file)
            return config