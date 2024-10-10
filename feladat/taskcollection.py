import feladat1
import json
class TaskCollection():
    def __init__(self):
        self.storage={}

    def add(self, task):
        if task.difficulty in self.storage.keys():
           self.storage[task.difficulty].append(task)
        else:
            self.storage[task.difficulty]=[task]
    def load(self, f):
        if f[-5:]!=".json":
            print("invalid file type")
        else:
            with open(f, 'r') as openfile:
                opened_file = json.load(openfile)
                opened_file={int(k):v for k,v in opened_file.items()}
                for k,v in opened_file.items():
                    for task in v:
                        self.add(feladat1.Task(task[0], k, task[1]))

    """def save(self, f):
        json_object = json.dumps(self.storage, indent=len(self.storage.keys()))
        with open(f, "w") as outfile:
            outfile.write(json_object)
    """