import json
import config

class Vent():
    def __init__(self):
        self.headers={"content-type":"application/json"} 
        self.body=""

    def add_body(self, text):
        self.body=text

    def export_vent(self):
        r = {
                "body": self.body
                }
        r = json.dumps(r) 
        return(r)


