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

    def save(self, f):
        tasks={}
        for k,v in self.storage.items():
            for task in v:
                l=task.serialize()
                if l[0] in tasks.keys():
                    tasks[l[0]].append([l[1], l[2]])
                else:
                    tasks[l[0]]=[[l[1],l[2]]]
        dupl=[]
        for key in tasks.keys():
            for i in range(len(tasks[key])-1):
                for j in range(i+1, len(tasks[key])):
                    if tasks[key][i]==tasks[key][j]:
                      dupl.append((key, tasks[key][i]))
        for (d,elt) in dupl:
            if elt in tasks[d]:
                tasks[d].remove(elt)
                        
        json_object = json.dumps(tasks, indent=len(tasks.keys()))
        with open(f, "w") as outfile:
            outfile.write(json_object)
    