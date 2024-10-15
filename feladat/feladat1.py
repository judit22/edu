import user

class Task():
    count=0
    def __init__(self, result, difficulty, task):
        self.result=result
        self.task=task
        self.difficulty=difficulty
        Task.count+=1
        self.index=Task.count
    
    def __str__(self):
        print(self.task, "=>",    )

    def serialize(self):
        return [self.difficulty, self.result, self.task]
    