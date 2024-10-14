import feladat1
import game
import user
import json

class History():
    def __init__(self):
        self.history={}
    def save(self, f):
        json_object = json.dumps(self.history, indent=len(self.history.keys()))
        with open(f, "w") as outfile:
            outfile.write(json_object)
    def load(self, f):
        if f[-5:]!=".json":
            print("invalid file type")
        else:
            with open(f, 'r') as openfile:
                opened_file = json.load(openfile)
                opened_file={k:v for k,v in opened_file.items()}
            self.history=opened_file
            return self
